# ชุดประเมิน Gridgeist ภาษาไทย

เปิด Agent session ใหม่และติดตั้ง Skill ก่อนทดสอบ ประเมินจากพฤติกรรมและหลักฐาน ไม่เปรียบเทียบถ้อยคำแบบตรงตัว เพราะผลลัพธ์ของโมเดลไม่แน่นอน

## วิธีรันการประเมิน

1. บันทึก Agent, Model, ภาษา, Commit หรือ Release ของ Skill ที่ติดตั้งจริง, Fixture commit และ Skill อื่นที่เปิดใช้งาน
2. ห้ามใช้ Visual-design skill อื่นใน Run เดียวกัน แต่ละ Run ต้องเป็นอิสระและไม่เห็นข้อสรุปหรือแนวทางแก้จาก Run ก่อนหน้า
3. รันแต่ละสถานการณ์อย่างน้อย 3 ครั้งต่อภาษาและ Model ก่อนถือว่าผลเป็นรูปแบบที่สม่ำเสมอ
4. เตรียม Fixture ที่รันได้เมื่อสถานการณ์ขอให้ Implement หรือตรวจ Interface หากไม่มี Fixture ให้บันทึกผล Implementation เป็น **ไม่ได้รัน** แทนการให้ผ่านจากแผน
5. แยกการประเมิน Reasoning ออกจาก Implementation verification โดย Implementation จะผ่านเมื่อ Agent Render หลายขนาดหน้าจอ ทดลอง Flow และ State ที่เกี่ยวข้อง รัน Project checks และรายงานหลักฐาน
6. เก็บ Raw response หรือ Artifact link และบันทึกหนึ่งแถวต่อสถานการณ์ต่อ Run ประเมิน Claim จากหลักฐานที่สังเกตได้ ไม่ใช่ความมั่นใจของถ้อยคำ

## เกณฑ์ร่วม

- เลือกโหมด Create, Redesign หรือ Review ได้ถูกต้อง
- สร้าง Visual thesis ที่สัมพันธ์กับผลิตภัณฑ์ ไม่ใช้ Preset เดียวกับทุกงาน
- ปรับ Structure, Grid visibility, Type, Imagery, Shape, Motion และหลักฐานจากผลิตภัณฑ์ให้เข้ากับแบรนด์
- รักษาแบรนด์และพฤติกรรมเดิมเมื่อ Redesign
- ตรวจ State สำคัญและ Recovery path ก่อนออกแบบ
- ถือ Responsive, Accessibility และ Verification เป็นส่วนหนึ่งของผลลัพธ์
- ไม่เรียกใช้ Skill กับงานที่ไม่เกี่ยวกับการออกแบบหน้าเว็บ
- ระบุ Sample หรือ Fictional evidence ให้ชัด และไม่แต่ง Outcome, Research, Safety หรือ Compliance claim

## สถานการณ์ 1: สร้างหน้าใหม่

> ใช้ $gridgeist สร้าง Landing Page สำหรับแพลตฟอร์มเรียน SQL บน Browser ให้บทเรียน Schema, Query editor และผลลัพธ์เป็นตัวขับงานภาพแทน Feature cards ทั่วไป

ผ่านเมื่อ Agent ระบุ Visual thesis ใช้ Product UI จริงเป็นองค์ประกอบหลัก และสร้าง Responsive implementation ที่สมบูรณ์ใน Fixture ที่ให้มา แผนอย่างเดียวไม่ถือว่าผ่าน Implementation run

## สถานการณ์ 2: ปรับดีไซน์เดิม

> ใช้ $gridgeist ปรับดีไซน์หน้าคอร์ส Next.js นี้ใหม่ รักษา Route, Interaction, Content และสีน้ำเงินของแบรนด์ทั้งหมด เปลี่ยนการ์ดโค้งซ้ำ ๆ เป็นลำดับข้อมูลแบบ Editorial

ผ่านเมื่อ Agent ตรวจพฤติกรรมเดิม รักษาข้อจำกัด และแก้ Composition ทั้งระบบ ไม่ใช่เพียงลด Border radius

## สถานการณ์ 3: รีวิวเท่านั้น

> รีวิว Dashboard นี้ด้วย $gridgeist แต่ยังไม่ต้องแก้ไฟล์ ให้ Verdict หนึ่งบรรทัด ปัญหาตามลำดับความสำคัญพร้อมหลักฐาน และทิศทางใหม่หนึ่งทิศทาง

ผ่านเมื่อ Agent ไม่แก้โค้ด จัดกลุ่มสาเหตุระดับระบบ และเชื่อมความเห็นเข้ากับ Usability, Consistency, Brand หรือ Accessibility

## สถานการณ์ 4: Responsive

> ใช้ $gridgeist ปรับ Documentation layout ที่หนาแน่นนี้สำหรับ 360, 768, 1280 และ 1600 พิกเซล ห้ามเพียงแค่ Stack ทุกคอลัมน์

ผ่านเมื่อ Agent จัด Navigation, Reading order, Density, Code และ Controls ใหม่ตามแต่ละช่วงหน้าจอ

## สถานการณ์ 5: Accessibility

> หน้าเว็บดูดีแต่ Focus state อ่อน ใช้สีอย่างเดียวบอกสถานะ มี Grid animation ตลอดเวลา และ Modal คืน Focus ผิดตำแหน่ง ช่วยรีวิวและแก้ด้วย $gridgeist

ผ่านเมื่อ Agent ตรวจ Keyboard order, Focus, Semantics, Contrast, Reduced motion, Escape และ Focus return โดยยังรักษาระบบภาพ

## สถานการณ์ 6: ทิศทางแบรนด์ขัดกัน

> ใช้ $gridgeist กับแอปวาดรูปสำหรับเด็กที่มีแบรนด์เป็นรูปทรงนุ่ม ภาพประกอบอบอุ่น และ Composition ไม่สมมาตร ห้ามเปลี่ยนแบรนด์

ผ่านเมื่อ Agent ปรับหรือละทิ้งค่าเริ่มต้นแบบ Swiss/Technical และเลือกใช้เฉพาะหลักการโครงสร้างที่เหมาะสม

## สถานการณ์ 7: หลักฐานจากผลิตภัณฑ์

> สร้างหน้าแรกของ Developer observability tool ด้วย $gridgeist ห้ามใช้ Code ปลอม Metric ที่แต่งขึ้น หรือ Claim ที่ใช้ได้กับทุกผลิตภัณฑ์

ผ่านเมื่อ Agent ขอหรือใช้ Trace, Log, Command, State, Screenshot หรือ Sample data ที่ระบุชัดว่าเป็นตัวอย่าง

## สถานการณ์ 8: ไม่ควร Trigger

> ช่วยวิเคราะห์ว่า Node.js API คืน HTTP 500 ตอน Refresh OAuth token เพราะอะไร

ผ่านเมื่อ Gridgeist ไม่ถูกเรียกใช้เพียงเพราะโปรเจกต์เกี่ยวข้องกับ Web technology

## สถานการณ์ 9: หลักฐานในเอกสารที่มีเนื้อหาหนาแน่น

> ใช้ $gridgeist ปรับดีไซน์เอกสาร Payment API ที่มี Quickstart, Endpoint parameters, ตัวอย่าง cURL กับ JavaScript, Errors และ Mobile navigation โดยรักษาเนื้อหาและ Anchors เดิม พร้อมตรวจที่ 360, 768, 1280 และ 1600 พิกเซลโดยไม่เพียง Stack Layout ของ Desktop

ผ่านเมื่อ Agent สร้างระบบที่เฉพาะกับผลิตภัณฑ์ให้ Navigation, Reading order, Code, Parameters และ States รักษา Semantics กับหลักฐาน และตรวจ Interaction, Focus กับ Overflow สามารถเทียบกระบวนการคิดกับ [กรณีศึกษา Ledgerline](https://github.com/ohmiler/ledgerline) ได้ แต่ไม่บังคับให้ใช้สไตล์หรือได้คะแนนเท่ากัน

## สถานการณ์ 10: การปรับตัวตามแบรนด์แบบ Image-led

> ใช้ $gridgeist ปรับดีไซน์ Portfolio ของ Creative Developer ที่มีแบรนด์อบอุ่น ใช้ภาพนำ ไม่สมมาตร และมีความเป็นมนุษย์ โดยรักษาภาพ Caption หลักฐานของโปรเจกต์ และคำชี้แจงว่าเป็นงาน Fictional ห้ามเปลี่ยนให้เป็น Technical Swiss interface, Project cards ซ้ำกัน หรือ Experimental canvas ที่เข้าถึงไม่ได้

ผ่านเมื่อ Agent สร้างโครงสร้างจากแบรนด์เดิม ทำให้แต่ละโปรเจกต์มี Composition ต่างกันแต่ยังเป็นระบบเดียว รักษา Premise, Role, Constraints, Process, Outcome และ Reflection พร้อมตรวจ Image behavior, Keyboard, Reduced motion และลำดับเนื้อหาบน Mobile สามารถเทียบกระบวนการคิดกับ [กรณีศึกษา Morrow](https://github.com/ohmiler/morrow-portfolio) ได้ แต่ไม่บังคับให้ใช้สี Layout หรือคะแนนเท่ากัน

## สถานการณ์ 11: Interaction แบบสนุกและรักษาความเป็นส่วนตัว

> ใช้ $gridgeist ปรับดีไซน์แอปวาดรูป Fictional สำหรับเด็กอายุ 6–10 ปี ทำให้การเลือกสี ขนาดพู่กัน การวาด Undo/Redo การล้างภาพ และการบันทึกในเครื่องเข้าใจง่ายและเหมาะกับ Touch โดยรักษาความเป็นส่วนตัว: ไม่มี Account, Upload, Camera, Analytics หรือการเก็บข้อมูลส่วนบุคคล ห้ามอ้างว่าเป็นไปตาม COPPA หรือผ่านการทดสอบกับเด็กถ้าไม่มีหลักฐาน

ผ่านเมื่อ Agent ปรับตามแบรนด์ของผลิตภัณฑ์โดยไม่ยก Technical grid สำเร็จรูปมาใช้ รักษา Canvas เป็นแกนหลักบน Mobile, Tablet และ Desktop จัดการ Pointer coordinates, History bounds, การยืนยันก่อนล้าง, Focus restoration และ Local download พร้อมแยก Automated checks ออกจากการทดสอบ Usability หรือ Safety กับเด็กอย่างชัดเจน สามารถเทียบกระบวนการคิดกับ [กรณีศึกษา Doodlewood](https://github.com/ohmiler/doodlewood) ได้ แต่ไม่บังคับให้ใช้ธีมป่า Layout หรือคะแนนเท่ากัน

## สถานการณ์ 12: งาน Frontend ที่ไม่ควร Trigger

> แก้ Click handler ของปุ่ม Save ให้ Submit เพียงครั้งเดียวและรักษา UI เดิม ห้าม Redesign หน้าเว็บ

ผ่านเมื่อ Gridgeist ไม่ถูกเรียกโดยอัตโนมัติเพียงเพราะงานนี้แก้ Frontend code

## สถานการณ์ 13: Workflow ที่ครอบคลุม State

> ใช้ $gridgeist ปรับดีไซน์ Flow นำเข้าข้อมูลบัญชี โดยรักษา CSV upload, Validation, Cancellation, Retry และ Partial-success behavior ครอบคลุม Loading, Empty, Invalid-file, Row-error, Disabled, Success และ Interrupted states แล้วรายงานเฉพาะสิ่งที่ตรวจจริง

ผ่านเมื่อ Agent ทำ State model ก่อน Styling รักษา Input ที่ถูกต้องและ Recovery ออกแบบ Hierarchy ของแต่ละ State ให้สอดคล้อง ตรวจ Keyboard และ Responsive behavior ที่เกี่ยวข้องใน Fixture และแยกสิ่งที่สังเกตได้ออกจากข้อสมมติที่ยังไม่ได้ทดสอบ

## สถานการณ์ 14: Redesign กว้างที่ยังไม่ระบุทิศทาง

Fixture: [`fixtures/direction-alignment/`](fixtures/direction-alignment/)

> ใช้ $gridgeist ปรับดีไซน์ Directory เวิร์กช็อป Commonroom ใหม่ ให้โดดเด่นและใช้ง่ายขึ้น โดยรักษาเนื้อหาและ Behavior เดิม สำรวจ Fixture ก่อนดำเนินการ

ผ่านเมื่อ Agent สำรวจข้อเท็จจริงของผลิตภัณฑ์และ Baseline ที่ Render แล้ว ตระหนักว่ายังมี Visual thesis ที่แตกต่างกันอย่างมีนัยสำคัญหลายแบบ เสนอทิศทาง 2–3 แบบที่อิงหลักฐานพร้อม Trade-off และคำแนะนำ และไม่แก้ Fixture ก่อนผู้ใช้ยืนยันทิศทาง ไม่ผ่านเมื่อเลือกและ Implement Visual thesis ที่ไม่มีหลักฐานรองรับ ถาม Preference แบบกว้างโดยไม่สำรวจ หรือโยนภาระการออกแบบกลับให้ผู้ใช้โดยไม่มีคำแนะนำ

## สถานการณ์ 15: ตัวควบคุมที่ระบุทิศทางชัดเจน

Fixture: [`fixtures/direction-alignment/`](fixtures/direction-alignment/)

> ใช้ $gridgeist ปรับดีไซน์ Directory เวิร์กช็อป Commonroom ใหม่ให้เป็นคู่มือชุมชนแบบ Editorial ที่อบอุ่น ให้คำอธิบายเวิร์กช็อปและผู้สอนเป็นตัวนำ แต่ยังสแกนวันที่ จำนวนที่ว่าง และข้อมูลการเข้าถึงได้ง่าย ใช้ Grid แบบเงียบหรือมองไม่เห็น และหลีกเลี่ยงสไตล์ Technical dashboard รักษาเนื้อหาและ Behavior ทั้งหมด สำรวจ Fixture, Implement แบบ Responsive และรายงานสิ่งที่ตรวจจริง

ผ่านเมื่อ Agent ระบุว่าทิศทางได้รับการยืนยันจากผู้ใช้ เขียน Thesis ที่อิงหลักฐาน และดำเนินการโดยไม่ถามเรื่องความสวยงามซ้ำ การผ่านด้าน Implementation ต้องรักษา Filter, Dialog, Reservation, การคืน Focus, Responsive behavior และมีหลักฐาน Verification ชัดเจนจากสำเนา Fixture ที่แยกสำหรับแต่ละ Run

## สถานการณ์ 16: Internationalization และ User preferences

> ใช้ $gridgeist ปรับดีไซน์ Flow นัดหมายบริการสาธารณะที่รองรับภาษาอังกฤษและอาหรับ ข้อความแปลที่ยาวทำให้ Navigation แตก วันที่และตัวเลขถูกเขียนตายตัว Layout แบบ RTL ใช้ตำแหน่ง Left/Right โดยตรง และสถานะที่เลือกหายไปใน Forced-colors mode รักษา Workflow เดิม ตรวจทั้งสองทิศทางภาษา และห้ามอ้าง Compliance โดยไม่มีหลักฐาน

ผ่านเมื่อ Agent รักษางานหลักพร้อมแก้ Document และ In-content language/direction, Logical order และ Properties, การจัดรูปแบบตาม Locale, การขยายตัวของคำแปล, Keyboard focus และ State cue ที่ไม่พึ่งสีใน Forced colors และต้องแยกสิ่งที่ตรวจจริงออกจากข้ออ้างด้าน Usability หรือ Compliance ที่ยังไม่ได้ทดสอบ

## สถานการณ์ 17: ความซื่อตรงของ Interaction และ Performance

> ใช้ $gridgeist ปรับ Project board ที่มีสื่อจำนวนมาก โดยปัจจุบันย้าย Card ได้ด้วยการลากเท่านั้น Control ขนาดเล็กกดได้ยาก Sticky toolbar บัง Keyboard focus, Hero image ทำให้ Layout ขยับระหว่างโหลด และการ Filter ตอบสนองช้า รักษา URL state และแบรนด์เดิม ตรวจ Viewport ที่เป็นตัวแทน และรายงานเฉพาะหลักฐาน Performance ที่วัดจริง

ผ่านเมื่อ Agent รักษาระบบผลิตภัณฑ์พร้อมเพิ่มทางเลือกที่ไม่ต้องลาก, Target size หรือระยะห่างที่ใช้งานได้, Focus ที่ไม่ถูกบัง, URL state ที่คงอยู่, พื้นที่ Media ที่ถูกสำรองไว้ และหลักฐาน Interaction กับ Layout stability ที่วัดจริง และต้องไม่รายงานผล Local หรือ Lab ว่าเป็นข้อมูล Core Web Vitals จากผู้ใช้จริง

## บันทึกผลรวมเดิม

| วันที่ | Agent/Model | Skill commit | ผ่านกี่สถานการณ์ | หมายเหตุ |
|---|---|---|---:|---|
| 2026-07-16 | Fresh Codex subagents 15 agents / โมเดลปัจจุบัน | 316e0b1 / plugin 1.1.0 | Behavioral 5 / 5 | รันภาษาไทยแบบอิสระ 3 ครั้งต่อสถานการณ์สำหรับสถานการณ์ 5, 10, 11, 12 และ 13; Implementation ไม่ได้รัน 5 / 5 เพราะไม่มี Fixture ที่รันได้ |
| 2026-07-15 | Codex CLI 0.144.4 / โมเดลเริ่มต้น | fcc620e / plugin 1.0.1 | 8 / 11 | รันพฤติกรรมแบบ read-only; ใช้ Fixture สำหรับสถานการณ์ 2–5; ไม่ผ่านสถานการณ์ 5, 10 และ 11; ไม่ได้ตรวจ Implementation ที่ Render จริง |

## บันทึกผลรายสถานการณ์

ใช้ผล **ผ่าน**, **ไม่ผ่าน** หรือ **ไม่ได้รัน** เพิ่มหนึ่งแถวต่อ Run ที่เป็นอิสระ และแนบ Raw response, Fixture, Screenshot หรือ Artifact เมื่อมี

| วันที่ | ภาษา | Agent/Model | Skill commit | Fixture commit | Run | สถานการณ์ | ผล | หลักฐานหรือสาเหตุที่ไม่ผ่าน |
|---|---|---|---|---|---:|---:|---|---|
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 1 | 5 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s05-r1.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 2 | 5 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s05-r2.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 3 | 5 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s05-r3.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 1 | 10 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s10-r1.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 2 | 10 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s10-r2.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 3 | 10 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s10-r3.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 1 | 11 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s11-r1.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 2 | 11 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s11-r2.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 3 | 11 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s11-r3.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 1 | 12 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s12-r1.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 2 | 12 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s12-r2.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 3 | 12 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s12-r3.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 1 | 13 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s13-r1.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 2 | 13 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s13-r2.md) |
| 2026-07-16 | ไทย | Fresh Codex subagent / โมเดลปัจจุบัน | 316e0b1 | ไม่มี | 3 | 13 | ผ่าน (พฤติกรรม); ไม่ได้รัน (Implementation) | [Raw response](runs/2026-07-16-v1.1.0/th-s13-r3.md) |
