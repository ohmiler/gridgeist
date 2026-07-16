**คำตัดสิน:** หน้าตาดีแต่ interaction layer ยังไม่พร้อมใช้งานจริง—focus มองเห็นยาก, สถานะพึ่งสี, motion รบกวนต่อเนื่อง และ modal คืน focus ผิด ทำให้ผู้ใช้คีย์บอร์ดและผู้ไวต่อการเคลื่อนไหวเสียบริบท

ข้อจำกัดของรีวิวนี้: ไม่มี target fixture หรือ rendered UI ให้ตรวจ จึงเป็นการวิเคราะห์จากอาการที่ระบุ ไม่ใช่ผลการ verify หน้าเว็บจริง และผมไม่ได้แก้ไฟล์ใน repository

### Findings และการแก้ที่ควรทำ

1. **Critical — Modal / ตอนปิด overlay**
   - **หลักฐาน:** ผู้ใช้ระบุว่า modal คืน focus ผิดตำแหน่ง
   - **ผลกระทบ:** ผู้ใช้คีย์บอร์ดหรือ screen reader หลุดจากจุดเริ่มงาน และอาจต้องไล่ Tab ใหม่ทั้งหน้า
   - **แก้ขั้นต่ำ:** ตอนเปิดให้บันทึก element ที่เป็นผู้เรียก modal; ย้าย focus เข้า modal ไปยัง heading หรือ control แรกที่เหมาะสม; trap focus ภายใน; ปิดด้วย `Escape`; ตอนปิดคืน focus ไปยัง trigger เดิมเฉพาะเมื่อ trigger ยังอยู่และใช้งานได้ หากถูกลบ ให้คืนไปยังจุดต่อเนื่องเชิงตรรกะ เช่น heading ของรายการหรือปุ่มเพิ่มรายการ ห้ามคืนไปที่ `body` หรือปุ่มคงที่ที่ไม่เกี่ยวข้อง

```ts
const opener = document.activeElement instanceof HTMLElement
  ? document.activeElement
  : null;

openDialog();
requestAnimationFrame(() => dialogTitle.focus());

function closeDialog() {
  closeDialogState();
  requestAnimationFrame(() => {
    if (opener?.isConnected && !opener.hasAttribute("disabled")) opener.focus();
    else logicalFallback.focus();
  });
}
```

ใช้ native `<dialog>` หรือ dialog primitive เดิมของโปรเจกต์ถ้ามี เพื่อไม่สร้าง focus trap เองโดยไม่จำเป็น

2. **High — Focus state / controls ทั้งหน้า**
   - **หลักฐาน:** ผู้ใช้ระบุว่า focus state อ่อน
   - **ผลกระทบ:** ตำแหน่งปัจจุบันไม่ชัด โดยเฉพาะบนพื้นผิวที่มี grid หรือ contrast สูง
   - **แก้ขั้นต่ำ:** กำหนด focus token เดียวที่มีทั้งความหนา ระยะห่าง และ contrast; ใช้ `:focus-visible` กับ link, button, input และ custom control ทุกชนิด; อย่าปิด `outline` หากไม่มี replacement ที่ชัดกว่า; ทดสอบทั้งพื้นสว่าง มืด selected และ error

```css
:root {
  --focus-ring: #0b63f6;
  --focus-offset: #fff;
}

:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 3px solid var(--focus-ring);
  outline-offset: 3px;
  box-shadow: 0 0 0 5px var(--focus-offset);
}
```

ถ้าพื้นหลังเปลี่ยนได้ ให้ token ของ offset อิง surface จริง ไม่ใช้สีขาวตายตัว

3. **High — Selected / success / warning / error states**
   - **หลักฐาน:** ผู้ใช้ระบุว่าใช้สีอย่างเดียวบอกสถานะ
   - **ผลกระทบ:** ผู้มีภาวะการมองเห็นสีแตกต่าง รวมถึงผู้ใช้จอ contrast ต่ำ อาจแยกสถานะไม่ได้
   - **แก้ขั้นต่ำ:** ให้ทุกสถานะมี cue เพิ่มอย่างน้อยหนึ่งแบบ เช่น icon พร้อมข้อความ, label, border pattern, weight หรือ shape และส่ง semantics ให้ assistive technology (`aria-current`, `aria-selected`, `aria-pressed`, `aria-invalid`, `role="status"`) ตามความหมายจริง ไม่ใส่ ARIA ซ้ำกับ native element

ตัวอย่าง: selected navigation ใช้ marker + น้ำหนักตัวอักษร + `aria-current="page"`; validation ใช้ icon + ข้อความที่ผูกด้วย `aria-describedby` ไม่ใช่เปลี่ยนเส้นขอบเป็นแดงอย่างเดียว

4. **High — Grid animation / พื้นหลังทั้งหน้า**
   - **หลักฐาน:** ผู้ใช้ระบุว่า grid เคลื่อนไหวตลอดเวลา
   - **ผลกระทบ:** ambient motion แข่งขันกับงานหลัก เพิ่มความล้า และอาจกระตุ้นอาการเวียนศีรษะ; grid ไม่ได้ทำหน้าที่อธิบายโครงสร้างอีกต่อไป
   - **แก้ขั้นต่ำ:** ทำ grid ให้หยุดนิ่งเป็นค่าเริ่มต้น หาก motion จำเป็นต่อเหตุและผล ให้เล่นเฉพาะช่วงสั้นเมื่อ state เปลี่ยนแล้วหยุด และปิด animation/transition ที่ไม่จำเป็นภายใต้ reduced motion

```css
.grid-surface {
  animation: none;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

อย่าซ่อน feedback สำคัญในโหมด reduced motion; เปลี่ยนเป็น state แบบทันทีแทน

### Replacement Direction

ออกแบบเป็นอินเทอร์เฟซสำหรับผู้ใช้ที่ต้องรักษาบริบทขณะทำงาน โดยใช้ grid แบบนิ่งเป็นโครงสร้าง, สถานะที่อ่านได้จากรูปทรงและภาษา, focus ring ที่เด่นสม่ำเสมอ และ motion เฉพาะเมื่ออธิบายเหตุ–ผลของการเปลี่ยนแปลง

ลำดับแก้ควรเป็น modal focus restoration → focus-visible system → non-color state cues → ลด grid motion จากนั้นจึงตรวจด้วยคีย์บอร์ดจริง: Tab/Shift+Tab, เปิด–ปิด modal ด้วย Enter และ Escape, trigger ที่ยังอยู่/ถูกลบ, selected/error/disabled states และ `prefers-reduced-motion` ที่ viewport ตัวแทนประมาณ 360, 768, 1280 และ 1600 px ก่อนจึงจะเรียกว่า verify ได้
