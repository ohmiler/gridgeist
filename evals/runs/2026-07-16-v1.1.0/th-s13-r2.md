# Direction

ข้อเสนอนี้เป็นสเปกการออกแบบ ไม่ใช่ผลจากการ implement หรือ render จริง

**Thesis:** พื้นที่ทำงานสำหรับผู้ดูแลบัญชีที่ต้องนำเข้าข้อมูลจำนวนมาก จัดลำดับตาม task flow แบบเป็นขั้น ใช้น้ำเสียงแม่นยำและสงบ และให้ “บัญชีแถวต่อแถว” เป็น product-native motif เพื่อให้ผู้ใช้เห็นว่าแต่ละแถวอยู่ตรงไหนของกระบวนการ

ใช้ grid แบบ quiet: โครงสร้างชัดจากแนวคอลัมน์ ลำดับ และเส้นแบ่งสถานะ แต่ไม่ทำให้หน้าดูเป็น technical dashboard โดยไม่จำเป็น สีต้องสืบทอด brand palette ที่มีอยู่และเพิ่ม semantic roles สำหรับ information, warning, error และ success; ไม่ใช้สีเป็นสัญญาณเพียงอย่างเดียว

# Flow ที่เสนอ

1. **เลือกไฟล์** — พื้นที่หลักมี drop zone และปุ่ม “เลือก CSV” พร้อมข้อความข้อกำหนดจริงของระบบ เช่น ขนาดสูงสุด encoding และชื่อคอลัมน์บังคับ โดยต้องดึงจากข้อจำกัดของผลิตภัณฑ์ ไม่สมมติค่าเอง
2. **ตรวจไฟล์** — หลังเลือกไฟล์ แสดงชื่อและขนาด แล้วตรวจ file-level rules ก่อนส่งข้อมูล เมื่อกำลัง parse หรือ upload ให้บอก phase จริง เช่น “กำลังอ่านไฟล์” หรือ “กำลังตรวจหัวตาราง”; แสดงเปอร์เซ็นต์เฉพาะเมื่อวัดได้จริง
3. **ตรวจแถว** — แสดงยอดรวม `ทั้งหมด / ใช้ได้ / มีข้อผิดพลาด` และ preview ที่ผูก error กับเลขแถวเดิม ชื่อฟิลด์ และวิธีแก้ ข้อมูลที่ถูกต้องต้องไม่หายเมื่อพบแถวผิด
4. **ยืนยันนำเข้า** — ถ้าทุกแถวถูกต้อง ใช้ “นำเข้า N บัญชี”; ถ้ามีทั้งแถวถูกและผิด ใช้คำสั่งชัดเจน “นำเข้าเฉพาะ N แถวที่ใช้ได้” และอธิบายว่าอีก M แถวจะไม่ถูกนำเข้า ห้ามทำ partial import โดยอัตโนมัติก่อนผู้ใช้ยืนยัน
5. **ประมวลผล** — แสดง progress ตามจำนวนแถวเมื่อ backend ให้ข้อมูลนั้นได้ ปิดการเปลี่ยนไฟล์และการกดเริ่มซ้ำ แต่คง action “ยกเลิก” ไว้หากระบบรองรับ
6. **สรุปผล** — แสดงจำนวน `นำเข้าสำเร็จ / ล้มเหลว / ข้าม / สถานะยังไม่ทราบ` พร้อม action ที่สอดคล้องกับผล: ดาวน์โหลด CSV ข้อผิดพลาด, ลองใหม่เฉพาะรายการที่ retry ได้, หรือเริ่มไฟล์ใหม่

# State contract

| สถานะ | สิ่งเด่นที่สุด | การกระทำและการเปลี่ยนสถานะ |
|---|---|---|
| `empty` | Drop zone, “เลือก CSV”, ข้อกำหนดไฟล์ | เลือกไฟล์ → `loading`; ไม่มี empty illustration ที่แย่งความสนใจจากงานหลัก |
| `loading` | ชื่อ phase, progress ที่วัดได้หรือ indeterminate, ชื่อไฟล์ | ปิด select/drop และ submit ซ้ำ; ยกเลิกได้ตาม phase; สำเร็จในการตรวจ → preview, ล้มเหลวระดับไฟล์ → `invalid-file`, การเชื่อมต่อขาด → `interrupted` |
| `invalid-file` | เหตุผลระดับไฟล์หนึ่งชุด เช่นชนิดไฟล์, encoding, header หรือขนาดไม่ผ่านกฎที่ตั้งไว้ | Primary action คือ “เลือกไฟล์อื่น”; เก็บข้อกำหนดไว้ให้เห็น ไม่เสนอ “ลองใหม่” หากไฟล์เดิมไม่มีทางผ่าน |
| `row-error` | Summary และรายการ error ต่อแถว โดยคงเลขแถวต้นฉบับ | ถ้าไม่มีแถวใช้ได้ ให้ปิด import; ถ้ามีบางแถวใช้ได้ ให้ยืนยัน partial import ได้; export error CSV และอัปโหลดไฟล์ที่แก้แล้วได้ |
| `disabled` | Control ยังอยู่ตำแหน่งเดิม พร้อมเหตุผลที่เข้าใจได้ | Import ถูกปิดเมื่อไม่มีไฟล์, validation ยังไม่จบ, ไม่มีแถวใช้ได้, กำลัง submit หรือกำลัง cancel; Retry ถูกปิดเมื่อไม่มีรายการที่ retry ได้หรือมี operation อื่นกำลังทำงาน |
| `success` | ผลลัพธ์แบบ full หรือ partial พร้อมจำนวนจริง | Full: “เสร็จแล้ว” และเริ่มไฟล์ใหม่; Partial: แยก imported กับ failed ชัดเจน พร้อมดาวน์โหลดข้อผิดพลาดและ retry เฉพาะแถวที่มีสิทธิ์ |
| `interrupted` | สถานะล่าสุดที่ยืนยันได้, เวลา/phase ล่าสุดถ้ามี, และรายการที่ยังไม่ทราบผล | Primary action คือ “ตรวจสอบสถานะต่อ” ก่อน retry; เมื่อ reconcile แล้วจึง retry เฉพาะ failed/unprocessed หรือกลับสู่ summary หากงานเสร็จแล้ว |

`disabled` ควรเป็นสถานะของ control ภายในแต่ละหน้าจอ ไม่ใช่หน้าจอปลายทางแยกต่างหาก และทุก control ที่ปิดควรมีข้อความใกล้เคียงอธิบายเงื่อนไขแทนการพึ่ง tooltip อย่างเดียว

# Cancellation, retry และ partial success

- ระหว่าง parse ฝั่งเครื่อง การยกเลิกหยุดงานทันทีและกลับไป `empty` โดยไม่สร้าง import job
- ระหว่าง upload, validation หรือ import ฝั่ง server ปุ่มเปลี่ยนเป็น “กำลังยกเลิก…” และห้ามสรุปว่า cancel สำเร็จก่อน server ตอบ เพราะบางแถวอาจ commit ไปแล้ว
- หากคำขอยกเลิกชนกับงานที่เสร็จพอดี ให้แสดงผลจริงจาก server ไม่ฝืนแสดง `interrupted`
- งานทุกครั้งควรมี stable import ID และการ submit/retry ควรมี idempotency contract; หากระบบยังไม่มี capability นี้ ต้องถือเป็นช่องว่างของ backend ไม่ใช่แก้ด้วยข้อความ UI
- Retry ต้องเริ่มจากการ reconcile import เดิมก่อน และส่งเฉพาะ row IDs ที่ failed แบบ transient หรือยังไม่ถูกประมวลผล ห้ามส่งแถวที่ imported แล้วซ้ำ
- Validation errors ที่ต้องแก้ข้อมูลใช้ action “ดาวน์โหลดข้อผิดพลาด” หรือ “อัปโหลดไฟล์ที่แก้แล้ว” ไม่เรียก retry แบบเดิมซ้ำ ส่วน transient server/network errors จึงใช้ “ลองใหม่” ได้
- Error CSV ควรคงเลขแถวเดิมและข้อมูลระบุตำแหน่ง พร้อม reason code/ข้อความแก้ไข แต่ต้องไม่เพิ่มข้อมูลอ่อนไหวเกินต้นฉบับ
- Partial success ไม่ใช้ banner “สำเร็จ” แบบเหมารวม: หัวข้อควรเป็น “นำเข้าแล้ว N จาก T บัญชี” และแสดง failed/skipped/unknown แยกกัน เพื่อไม่ทำให้ผู้ใช้คิดว่างานจบสมบูรณ์

# Responsive และ interaction requirements

- Desktop ให้ summary และ action อยู่ในแนวคงที่เหนือ row ledger; ตารางมี header ติดตามการเลื่อนเฉพาะเมื่อไม่บังเนื้อหาและต้องมีการจัดการ overflow จริง
- Mobile จัดใหม่เป็น `summary → primary action → filters → row errors`; แต่ละ error ใช้ disclosure ต่อแถวแทนการบีบทุกคอลัมน์ และคงเลขแถวกับเหตุผลไว้เสมอ
- Primary action ต้องไม่ย้ายตำแหน่งอย่างรุนแรงเมื่อ error ปรากฏ เพื่อลดการกดผิด และ sticky action bar ต้องไม่บังแถวสุดท้ายหรือ keyboard
- Drop zone ต้องมีปุ่มเลือกไฟล์ที่ใช้งานด้วย keyboard ได้; drag-and-drop เป็นทางเสริม ไม่ใช่ทางเดียว
- Status ใช้ icon/label/count ร่วมกับสี, error summary รับ focus หลัง validation, focus ของ dialog ยกเลิกต้องคืนสู่ trigger และ progress update ควรประกาศแบบไม่ถี่จนรบกวน screen reader
- Motion ใช้เพื่อบอก phase change หรือ progress เท่านั้น และต้องรองรับ reduced motion โดยไม่ซ่อนข้อมูลสถานะ

# สิ่งที่ตรวจสอบจริง

ตรวจโดยตรงเฉพาะหลักการใน `gridgeist/SKILL.md`, `references/design-language.md` และ `references/review-checklist.md` แล้วใช้หลัก transactional workflow, state inventory, recovery, responsive recomposition และการแยก observed evidence ออกจาก inference มาสร้างสเปกข้างต้น

ไม่มี fixture, UI, โค้ด, brand tokens, API contract หรือ runtime ให้ตรวจ จึง **ไม่ได้** render viewport, ทดลอง mouse/touch/keyboard, ตรวจ focus จริง, ทดสอบ cancellation race, ยืนยัน idempotency, รัน lint/test/build หรือรับรอง accessibility/usability/compliance ข้อกำหนดทั้งหมดข้างต้นจึงเป็น direction และ acceptance contract ที่ยังต้องยืนยันกับผลิตภัณฑ์และ backend ก่อน implementation
