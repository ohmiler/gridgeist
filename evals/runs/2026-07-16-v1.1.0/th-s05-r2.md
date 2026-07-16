**คำตัดสิน:** หน้าตาอาจเรียบร้อย แต่ interaction system ยังไม่พร้อมสำหรับผู้ใช้คีย์บอร์ดและผู้ใช้ที่ไวต่อการเคลื่อนไหว; ควรแก้ทั้งสี่จุดเป็นระบบเดียวก่อนเพิ่มงาน polish

ข้อค้นพบนี้อิงจากอาการที่คุณระบุเท่านั้น ผมยังไม่ได้เห็น DOM, CSS, component หรือหน้าที่ render จึงไม่อ้างว่าได้แก้หรือยืนยันผลบนของจริงแล้ว

1. **สูง — Focus state อ่อน**
   - ตำแหน่ง: control ที่โต้ตอบได้ทั้งหมด โดยเฉพาะ navigation, ปุ่มเปิด Modal และ action ใน Modal
   - หลักฐาน: คุณระบุว่า focus มองเห็นยาก
   - ผลกระทบ: ผู้ใช้คีย์บอร์ดไม่รู้ว่าคำสั่งถัดไปจะเกิดที่ใด
   - แก้ขั้นต่ำ: ใช้ focus token เดียวทั้งระบบกับ `:focus-visible` เช่น `outline: 2px solid var(--focus-ring); outline-offset: 3px;` ให้มี contrast กับพื้นผิวรอบข้างอย่างชัดเจน และอย่าปิด `outline` จนกว่าจะมีสิ่งทดแทนที่เทียบเท่า ตรวจทุกสถานะทั้ง default, hover, active, selected, disabled และ destructive

2. **สูง — ใช้สีอย่างเดียวสื่อสถานะ**
   - ตำแหน่ง: selected/active/success/warning/error และสถานะใน Grid
   - หลักฐาน: คุณระบุว่าสถานะแยกกันด้วยสีเพียงอย่างเดียว
   - ผลกระทบ: ผู้ใช้ที่แยกสีได้ยากหรือใช้โหมด contrast สูงอาจพลาดข้อมูลสำคัญ
   - แก้ขั้นต่ำ: ให้ทุกสถานะมี cue อย่างน้อยอีกหนึ่งชนิด เช่น ข้อความหรือไอคอนพร้อม accessible name, border/weight/shape ที่เปลี่ยน, และ semantic state ที่ตรงชนิด (`aria-current`, `aria-selected`, `aria-pressed`, `checked`, `aria-invalid`) ตัวอย่าง error ควรมีข้อความอธิบายและวิธีกู้คืน ไม่ใช่แค่กรอบแดง

3. **สูง — Grid animation ทำงานตลอดเวลา**
   - ตำแหน่ง: พื้นหลังหรือ Grid layer ที่เคลื่อนไหวต่อเนื่อง
   - หลักฐาน: คุณระบุว่า animation ไม่หยุด
   - ผลกระทบ: แย่งความสนใจจากงานหลัก เพิ่มภาระการรับรู้ และอาจกระทบผู้ใช้ที่ไวต่อ motion
   - แก้ขั้นต่ำ: เปลี่ยน Grid ให้เป็นโครงสร้างนิ่งโดยค่าเริ่มต้น ใช้ motion เฉพาะเมื่ออธิบายเหตุและผล เช่น state transition สั้นครั้งเดียว หยุดเมื่อ element อยู่นอก viewport หรือหน้าไม่ active และรองรับ:

```css
@media (prefers-reduced-motion: reduce) {
  .grid-motion {
    animation: none;
    transition: none;
  }
}
```

อย่าซ่อนข้อมูลสำคัญเมื่อปิด motion; แสดง end state ให้ครบแทน

4. **สูง — Modal คืน focus ผิดตำแหน่ง**
   - ตำแหน่ง: วงจรเปิด–ใช้งาน–ปิด Modal
   - หลักฐาน: คุณระบุว่า focus กลับไปยังตำแหน่งที่ไม่ถูกต้อง
   - ผลกระทบ: ผู้ใช้คีย์บอร์ดเสียบริบทและอาจต้องไล่ Tab ใหม่ทั้งหน้า
   - แก้ขั้นต่ำ: ตอนเปิดให้บันทึก `document.activeElement` ซึ่งควรเป็น trigger จริง; ย้าย focus ไป heading หรือ control แรกที่เหมาะสมใน Modal; จำกัด Tab ภายใน Modal; ปิดด้วย Escape; ตอนปิดคืน focus ไป trigger เดิมเฉพาะเมื่อยังอยู่ใน DOM และใช้งานได้ หาก trigger ถูกลบ ให้คืนไปยัง fallback ที่มีเหตุผลใน workflow เช่นหัวข้อหรือ action ของรายการข้างเคียง ห้ามคืนไป `body` หรือ element ตามตำแหน่ง DOM แบบตายตัว

**Direction ทดแทน:** ใช้ grid เป็นโครงสร้างนิ่งที่ช่วยจัดลำดับงาน ให้สถานะมีทั้งรูปทรง/ข้อความ/semantic state และใช้ motion สั้น ๆ เฉพาะเพื่ออธิบายการเปลี่ยนแปลง โดย focus เป็นชั้น interaction ที่เด่นและสม่ำเสมอที่สุด

เกณฑ์ตรวจรับหลังนำไปแก้:

- เดินทั้ง flow ด้วย Tab, Shift+Tab, Enter/Space และ Escape โดยไม่ใช้เมาส์; focus ต้องมองเห็นและเรียงตามงาน
- เปิด–ปิด Modal จาก trigger หลายตำแหน่ง รวมกรณี trigger ถูกลบหรือ disabled; focus ต้องกลับสู่จุดที่คาดเดาได้
- ตรวจทุกสถานะใน grayscale และโหมด forced colors; ความหมายต้องไม่หายเมื่อไม่มีสี
- เปิด `prefers-reduced-motion: reduce`; Grid ต้องหยุดแต่ข้อมูลและ feedback ยังครบ
- ตรวจอย่างน้อยที่ประมาณ 360, 768, 1280 และ 1600 px รวม zoom และ label ยาว

สิ่งที่ยังต้องตรวจจากของจริงคือ contrast ของ focus ring, ลำดับ focus, semantics ของ control, focus trap, breakpoint และพฤติกรรม animation เมื่อเปลี่ยน visibility; รายการข้างต้นคือ correction spec ไม่ใช่ผล verification
