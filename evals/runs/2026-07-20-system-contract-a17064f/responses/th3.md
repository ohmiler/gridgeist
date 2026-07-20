ปรับ Account workspace เรียบร้อยแล้ว โดยแก้เฉพาะ [styles.css](C:/tmp/gridgeist-s19-eval-a17064f-20260720/th3/styles.css)

- สร้าง foundation และ semantic tokens สำหรับสี ระยะห่าง radius surface และ interaction states
- รวม grammar ของ Card, Button, Input และ Status badge ให้สอดคล้องกัน
- รักษาทิศทาง blue-gray ที่มีอยู่ พร้อม light/dark theme
- ปรับ responsive composition สำหรับ 360, 768 และ 1280px
- รักษา routes, navigation และ behavior เดิมทั้งหมด
- เพิ่ม reduced-motion และ forced-colors treatment

ตรวจด้วย browser จริงแล้ว:

- Theme toggle และ dark theme
- Profile save: loading/disabled → success
- Invoice filtering, preparation และ plan feedback
- ไม่มี horizontal overflow ที่ viewport ตัวแทน
- ไม่มี console errors
- `DESIGN.md` ไม่ถูกแก้ไข และไม่ได้สร้างเอกสารดีไซน์ใหม่
- ปิด browser และ local preview server แล้ว
