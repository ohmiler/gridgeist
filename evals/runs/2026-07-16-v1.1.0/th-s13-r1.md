# Behavioral evaluation: การนำเข้าข้อมูลบัญชีด้วย CSV

## ขอบเขตและคำตัดสิน

ยังประเมินหน้าจอจริงไม่ได้ เพราะคำขอนี้ไม่มี fixture, implementation หรือ rendered UI ให้ตรวจ ผลด้านล่างจึงเป็นข้อกำหนดการออกแบบเชิงพฤติกรรม ไม่ใช่ผลยืนยันว่า flow ถูก implement, render หรือใช้งานได้จริง

## Direction

**Thesis:** พื้นที่ทำงานสำหรับผู้ดูแลบัญชีที่จัดลำดับตามงาน “เลือกไฟล์ → ตรวจสอบ → ยืนยัน → นำเข้า → แก้ไข/ลองใหม่” ใช้โครงสร้างแบบ transactional ที่นิ่งและแม่นยำ พร้อมสถานะระดับไฟล์ แถว และงานนำเข้าที่มองเห็นได้ตลอดเวลา

- ให้ตาราง preview และผลตรวจเป็น visual lead; ใช้ grid แบบ quiet เพื่อคง alignment โดยไม่ทำให้หน้าดูเหมือน dashboard ทั่วไป
- วางชื่อขั้นตอน สถานะรวม และ primary action ในตำแหน่งคงที่ เพื่อลด disruptive reflow เมื่อเกิด error
- ยังไม่มีหลักฐานเรื่อง brand, typography, palette หรือ component system จึงไม่กำหนดฟอนต์ สี หรือรูปทรงเฉพาะแบรนด์ ให้ใช้ token และ primitive เดิมของผลิตภัณฑ์เมื่อมี

## Flow ที่เสนอ

1. **เลือกไฟล์** — drop zone และปุ่มเลือกไฟล์รับ CSV หนึ่งไฟล์ พร้อมบอกข้อกำหนดที่ทราบจริงจากระบบ เช่น ขนาดสูงสุด encoding และคอลัมน์บังคับ หากยังไม่ทราบ ห้ามแต่งค่าขึ้นเอง
2. **ตรวจระดับไฟล์** — ตรวจชนิดไฟล์, ความสามารถในการอ่าน, encoding, header, schema, คอลัมน์ซ้ำ/ขาด และจำนวนแถว ก่อนเปิดทางให้ import ความผิดพลาดระดับนี้หยุดทั้งไฟล์
3. **ตรวจระดับแถว** — แสดง preview พร้อมเลขแถว ฟิลด์ที่ผิด เหตุผล และวิธีแก้ สรุปจำนวน `พร้อมนำเข้า / มีข้อผิดพลาด / ทั้งหมด` โดยไม่ลบแถวที่ valid
4. **ยืนยันขอบเขต** — ผู้ใช้เลือกได้อย่างชัดเจนว่าจะนำเข้าเฉพาะแถว valid หรือยกเลิกเพื่อแก้ CSV หากนโยบายระบบไม่อนุญาต partial import ให้ปิด action พร้อมเหตุผลแทนการซ่อนปุ่ม
5. **นำเข้า** — แยกสถานะ upload, validating และ importing; แสดง progress ที่มีความหมายจาก backend ไม่ใช้เปอร์เซ็นต์จำลอง ปุ่มยกเลิกต้องระบุผลที่จะเกิดขึ้นก่อนกด
6. **สรุปผล** — แสดงจำนวนสำเร็จ ล้มเหลว ข้าม และยังไม่ประมวลผล พร้อมไฟล์ข้อผิดพลาดหรือรายการแถวที่แก้ได้ จากนั้นให้ `ลองใหม่เฉพาะแถวที่ล้มเหลว` และ `นำเข้าไฟล์ใหม่`

## State และ recovery contract

| สถานะ | สิ่งที่ผู้ใช้เห็น | การกระทำและกติกา |
|---|---|---|
| `empty` | drop zone, ปุ่มเลือกไฟล์ และข้อกำหนดไฟล์; ถ้า CSV มี header แต่ไม่มี data row ให้บอกว่า “ไม่พบข้อมูลบัญชี” | Import disabled; เปลี่ยนไฟล์หรือยกเลิกได้ ไม่แสดงเป็น generic error |
| `loading` | label ตามช่วงงาน (`กำลังอัปโหลด`, `กำลังตรวจสอบ`, `กำลังนำเข้า`), progress เมื่อ backend ให้ค่าจริง และ live status ที่ไม่แย่ง focus | ป้องกัน submit ซ้ำ; อนุญาต cancel เฉพาะช่วงที่ระบบรองรับ; reload/ออกจากหน้าต้องไม่ทำให้ผู้ใช้เข้าใจผิดว่างานหยุดแล้ว |
| `invalid-file` | banner ระดับไฟล์ที่บอกสาเหตุจำเพาะ เช่น อ่านไม่ได้, header ไม่ครบ หรือชนิดไม่รองรับ | ไม่เริ่ม import; คงหน้าจอให้เลือกไฟล์ใหม่; focus ไปยังสรุป error และผูกข้อความกับ input |
| `row-error` | summary และตารางที่ระบุเลขแถว ฟิลด์ ค่าเมื่อเปิดเผยได้ และเหตุผล โดยมี non-color cue | เก็บแถว valid; filter ไปยังแถวผิดได้; เปิด partial import ตาม policy หรือปิดพร้อมเหตุผล; validation error ต้องแก้ไฟล์ก่อน retry |
| `disabled` | control ยังคงมองเห็น มี label และเหตุผลใกล้ปุ่ม เช่น “ยังไม่มีแถวที่พร้อมนำเข้า” | ใช้ native disabled เมื่อเหมาะสม แต่เหตุผลต้องอ่านได้โดยไม่ต้อง hover; ห้ามใช้สีเพียงอย่างเดียว |
| `success` | จำนวนที่นำเข้าสำเร็จและผลที่ตรวจสอบย้อนกลับได้ | เมื่อสำเร็จทั้งหมด ให้ primary action ไปยังรายการบัญชี; secondary action นำเข้าไฟล์ใหม่; ไม่ใช้ toast เป็นหลักฐานเพียงจุดเดียว |
| `partial-success` | แยกจำนวนสำเร็จ ล้มเหลว ข้าม และไม่ประมวลผลอย่างชัดเจน | แถวสำเร็จต้องไม่ถูกนำเข้าซ้ำ; ให้ดาวน์โหลด/คัดกรอง error และ retry เฉพาะแถวที่ล้มเหลวด้วย idempotency contract |
| `interrupted` | บอกว่างานถูกขัดจังหวะจากผู้ใช้ เครือข่าย หรือระบบ และแสดงสถานะล่าสุดที่ backend ยืนยัน | ถ้ามี job ID ให้ resume/poll งานเดิม; ถ้าไม่มี ให้บอกว่าไม่ทราบผลและตรวจสอบรายการบัญชีก่อนลองใหม่ ห้ามรีเซ็ตเป็น empty แบบเงียบ ๆ |

## Cancellation, retry และ partial success

- **ก่อนเริ่ม import:** cancel ทิ้ง selection/preview หลังเตือนเฉพาะเมื่อมีงานที่ผู้ใช้ทำไว้ และกลับจุดเดิมโดยไม่เขียนข้อมูล
- **ระหว่าง upload/validation:** abort request ได้เมื่อ backend รองรับ และกลับสู่สถานะที่เลือกไฟล์ใหม่ได้
- **ระหว่าง import:** ต้องกำหนด semantics จากระบบจริงว่าเป็น atomic ทั้งไฟล์หรือ atomic รายแถว หากรายแถว การ cancel หยุดเฉพาะงานที่ยังไม่ commit และผลลัพธ์เป็น `interrupted` พร้อมยอด committed/failed/pending
- **retry:** ใช้ job/import identifier และ idempotency key เพื่อไม่สร้างบัญชีซ้ำ retry อัตโนมัติเฉพาะ transient failure แบบจำกัดครั้ง; validation error ต้องให้ผู้ใช้แก้ข้อมูล
- **partial success:** ห้ามเรียกว่า success เฉย ๆ และห้าม rollback แถวที่สำเร็จโดยปริยาย แสดงขอบเขตผลลัพธ์พร้อมทาง recovery ที่รักษาข้อมูล valid

## Responsive และ accessibility contract

- Desktop ใช้ summary คงที่เหนือ table; mobile เปลี่ยนแต่ละแถวเป็นลำดับ `เลขแถว → ฟิลด์ → เหตุผล → วิธีแก้` โดยไม่บีบตารางกว้าง
- primary action และ cancel ต้องคงลำดับความสำคัญเดิมทุก breakpoint และมี touch target ที่เหมาะสม
- ใช้ semantic headings, label, button และ table/list ตามโครงสร้างจริง; keyboard order ต้องตาม flow
- เมื่อ validation จบ ให้ประกาศ summary ผ่าน live region แต่ไม่ย้าย focus ออกจากผู้ใช้โดยไม่จำเป็น; เมื่อ submit ล้มเหลวให้ focus error summary ซึ่งลิงก์ไปยังแถวผิด
- รองรับ visible focus, zoom, ข้อความยาว/ภาษาแปล และ `prefers-reduced-motion`; สถานะทุกชนิดต้องมีข้อความหรือสัญลักษณ์นอกเหนือจากสี

## สิ่งที่ตรวจสอบจริง

- อ่าน `skills/gridgeist/SKILL.md` และ references ที่ workflow อ้างโดยตรงคือ `design-language.md` กับ `review-checklist.md`
- ตรวจว่าข้อกำหนดที่เสนอนี้ครอบคลุม CSV upload, file/row validation, cancellation, retry, partial success และสถานะ `loading`, `empty`, `invalid-file`, `row-error`, `disabled`, `success`, `interrupted`
- ไม่ได้อ่าน source UI, routes, components, tokens, product policy, schema บัญชี หรือ brand assets
- ไม่ได้ render viewport ใด ไม่ได้ exercise mouse/touch/keyboard flow ไม่ได้รัน formatter, typecheck, lint, test หรือ build และไม่ได้ตรวจ screen reader/contrast
- ดังนั้น behavior, responsive layout, accessibility, backend atomicity, idempotency และ recovery ทั้งหมดยังเป็นข้อเสนอที่ต้องยืนยันกับ implementation และนโยบายข้อมูลจริง
