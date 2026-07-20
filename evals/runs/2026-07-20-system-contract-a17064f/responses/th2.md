ปรับ Account workspace เรียบร้อยแล้ว โดยรักษา routes, เนื้อหา และ behavior เดิมทั้งหมด

**Direction**

Workspace สำหรับจัดการบัญชีที่สุขุมและอ่านสถานะได้เร็ว ใช้ quiet grid, blue-gray identity เดิม และสถานะ workspace/invoice เป็น visual motif หลัก

**Implementation**

- รวม foundation และ semantic tokens สำหรับสี, spacing, radius, surface, focus และ light/dark theme ใน [styles.css](C:/tmp/gridgeist-s19-eval-a17064f-20260720/th2/styles.css)
- สร้าง component conventions ร่วม: `surface`, `stat-card`, `badge--*`, `button--*`
- ปรับ responsive composition สำหรับ navigation, metrics, forms, plan และ invoices
- เพิ่ม reduced-motion และ forced-colors safeguards
- อัปเดต class composition ใน [index.html](C:/tmp/gridgeist-s19-eval-a17064f-20260720/th2/index.html) และ [billing.html](C:/tmp/gridgeist-s19-eval-a17064f-20260720/th2/billing.html)
- ไม่แก้ `DESIGN.md`, `script.js`, routes หรือสร้างเอกสารดีไซน์ใหม่

**Verification**

ตรวจด้วย browser จริง:

- Profile light/dark ที่ 1280×900
- Billing dark ที่ 360×800 โดยไม่มี horizontal overflow
- Navigation และ theme persistence
- Profile save และ success feedback
- Invoice filtering/count, Prepare และ Manage plan feedback
- Console: 0 errors, 0 warnings

ปิด browser และ local preview serverแล้ว พร้อมลบ verification artifacts ออกจาก workspace แล้วครับ