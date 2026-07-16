**คำตัดสิน:** หน้าตาดี แต่ interaction layer ยังสื่อสถานะไม่ครบและรบกวนการใช้งานด้วยคีย์บอร์ด; ควรแก้ทั้งสี่จุดก่อนถือว่าประสบการณ์หลักพร้อมใช้งาน

หลักฐานในรอบนี้มาจากอาการที่คุณรายงานเท่านั้น ผมไม่ได้รับ target fixture หรือหน้าที่ render จึงยังไม่ได้แก้ไฟล์หรือยืนยันผลจากการทดสอบจริง

### Findings ตามลำดับความสำคัญ

1. **High — Modal คืน focus ผิดตำแหน่ง**
   - **ตำแหน่ง:** ทุก modal/dialog และ trigger ที่เปิดมัน
   - **หลักฐาน:** รายงานว่าเมื่อปิด modal แล้ว focus ไปผิดจุด
   - **ผลกระทบ:** ผู้ใช้คีย์บอร์ดหรือ screen reader สูญเสียบริบทและต้องไล่หา action เดิมใหม่
   - **แก้ขั้นต่ำ:** เก็บ element ที่เปิด modal *ก่อน* เปิด, ย้าย focus เข้า dialog ไปยัง control แรกที่มีความหมาย (หรือหัว dialog ที่มี `tabindex="-1"`), จำกัด Tab ให้อยู่ใน dialog, ปิดได้ด้วย Escape และเมื่อปิดให้คืน focus ไปยัง opener หากยังอยู่ใน DOM; ถ้า opener หาย ให้ใช้ fallback ที่สมเหตุผล เช่น heading หรือปุ่มของรายการเดิม ห้ามคืนไป `body`

2. **High — Focus state อ่อน**
   - **ตำแหน่ง:** link, button, input, select, textarea, custom control และปุ่มปิด modal
   - **หลักฐาน:** รายงานว่า focus มองเห็นยาก
   - **ผลกระทบ:** ผู้ใช้คีย์บอร์ดไม่ทราบตำแหน่งปัจจุบัน โดยเฉพาะบนพื้นหลังหลายโทน
   - **แก้ขั้นต่ำ:** ใช้ `:focus-visible` เป็น token ระดับระบบที่เปลี่ยนมากกว่าสี เช่น outline 2–3px พร้อม offset และมี contrast ชัดทั้งพื้นสว่าง/มืด อย่าใช้ `outline: none` เว้นแต่มี replacement ที่เทียบเท่า และรองรับ forced-colors

```css
:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 3px solid var(--focus-ring);
  outline-offset: 3px;
  box-shadow: 0 0 0 1px var(--surface);
}

@media (forced-colors: active) {
  :where(a, button, input, select, textarea, [tabindex]):focus-visible {
    outline-color: Highlight;
    box-shadow: none;
  }
}
```

3. **High — ใช้สีอย่างเดียวบอกสถานะ**
   - **ตำแหน่ง:** selected/active, success/error/warning และสถานะใน grid
   - **หลักฐาน:** รายงานว่าสถานะแยกกันด้วยสีเพียงอย่างเดียว
   - **ผลกระทบ:** ผู้ใช้ที่แยกสีได้ยาก รวมถึงผู้ใช้ screen reader อาจไม่รับรู้ความหมาย
   - **แก้ขั้นต่ำ:** เพิ่ม cue ที่ไม่พึ่งสีอย่างน้อยหนึ่งชนิด เช่น icon + ข้อความ, เส้น/รูปทรง, น้ำหนักตัวอักษร หรือเครื่องหมาย check พร้อม semantic state ที่ถูกต้อง (`aria-current`, `aria-selected`, `aria-pressed`, `aria-invalid` ตามชนิด control) ข้อความ error ควรเชื่อมด้วย `aria-describedby`; อย่าใส่ ARIA เพื่อชดเชย element ที่ควรเป็น native button/input

4. **Medium — Grid animation ทำงานตลอดเวลา**
   - **ตำแหน่ง:** animated grid/background ทั่วหน้า
   - **หลักฐาน:** รายงานว่า animation ไม่หยุด
   - **ผลกระทบ:** แย่งความสนใจจากงานหลักและอาจกระตุ้นอาการจาก motion
   - **แก้ขั้นต่ำ:** ให้ motion เกิดจากเหตุและจบเอง ไม่ใช่ ambient loop; ถ้าจำเป็นต่อแบรนด์ ให้เล่นสั้น ๆ แล้วหยุดและมี pause control เมื่อเกินช่วงสั้น รองรับ `prefers-reduced-motion` โดยปิดการเคลื่อนที่ แต่คง state สำคัญไว้

```css
@media (prefers-reduced-motion: reduce) {
  .grid-animation {
    animation: none;
    transform: none;
  }
}
```

### Direction ทดแทน

สำหรับผู้ใช้ที่ต้องอ่านสถานะและทำงานต่อเนื่อง ให้โครง grid เป็นระบบจัดวางที่นิ่งและเงียบ ใช้ motion เฉพาะ feedback ที่มีเหตุ และทำให้ focus/selected/error เป็นภาษาสถานะร่วมกันผ่านรูปทรง ข้อความ และ semantics โดยไม่เปลี่ยนบุคลิกภาพเดิมของแบรนด์

### เกณฑ์รับงานหลังนำไปแก้

- ไล่ Tab/Shift+Tab ผ่าน flow หลักแล้วเห็น focus ชัดทุกจุด และลำดับตรงกับงาน
- เปิด modal จากหลาย trigger, ใช้ Tab/Shift+Tab, ปิดด้วย Escape/ปุ่มปิด แล้ว focus กลับ trigger เดิมหรือ fallback ที่กำหนด
- ปิดสีหรือดูใน grayscale แล้วยังแยก selected, error, success และ disabled ได้
- เปิด reduced motion แล้ว grid หยุด โดยข้อมูลและ feedback สำคัญไม่หาย
- ทดสอบอย่างน้อยที่ 360, 768, 1280 และ 1600px รวมถึง keyboard และ screen reader flow

รายการนี้เป็นแผนแก้และเกณฑ์ตรวจ ไม่ใช่ผล verification; ต้องทดสอบกับหน้า render จริงหลัง implementation อีกครั้ง
