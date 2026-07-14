# Gridgeist — คู่มือภาษาไทย

[English](README.md) · **ภาษาไทย** · [เว็บไซต์](https://ohmiler.github.io/gridgeist/th/) · [ตัวอย่าง](https://ohmiler.github.io/gridgeist/examples/)

Gridgeist คือ Agent Skill สำหรับสร้าง ปรับดีไซน์ และรีวิวหน้าเว็บด้วยระบบกริดที่ชัดเจน การจัดตัวอักษรที่แม่นยำ และลำดับข้อมูลที่มีเหตุผล ช่วยลดหน้าตาแบบ Generic AI SaaS โดยยังรักษาแบรนด์ ฟังก์ชัน Responsive behavior และ Accessibility ของผลิตภัณฑ์

## เห็นความต่างได้ทันที

ตัวอย่าง Northline Logistics นี้สร้างจากหน้า HTML/CSS แบบเต็มสองเวอร์ชัน โดยใช้ผลิตภัณฑ์ เนื้อหา ข้อมูล และขนาดหน้าจอชุดเดียวกัน

<table>
  <tr>
    <th width='50%'>ไม่ใช้ Gridgeist - Generic SaaS</th>
    <th width='50%'>ใช้ Gridgeist - ระบบที่สะท้อนผลิตภัณฑ์</th>
  </tr>
  <tr>
    <td><img src='docs/assets/northline-before.png' alt='หน้าเว็บ Northline Logistics แบบ Generic ที่ใช้ข้อความการตลาด กราฟ และการ์ดตัวเลขซึ่งพบได้ทั่วไป' width='100%' /></td>
    <td><img src='docs/assets/northline-after.png' alt='หน้าเว็บ Northline Logistics ที่จัดระบบจากเส้นทางขนส่ง สถานะเที่ยวขนส่ง เวลาถึง และข้อมูลปฏิบัติการจริง' width='100%' /></td>
  </tr>
</table>

เนื้อหาและข้อมูลปฏิบัติการเหมือนเดิม แต่ใช้ระบบการออกแบบต่างกัน Gridgeist เปลี่ยนภาพลักษณ์จากการ์ดทั่วไปให้เป็นเครือข่ายขนส่งที่สร้างจากหลักฐานของผลิตภัณฑ์ [เปิดหน้า Before](https://ohmiler.github.io/gridgeist/readme-showcase/?view=before) หรือ [เปิดหน้า After](https://ohmiler.github.io/gridgeist/readme-showcase/?view=after)

## เริ่มใช้ใน 60 วินาที

1. ดาวน์โหลด Repository นี้:

   ```shell
   git clone https://github.com/ohmiler/gridgeist.git
   ```

2. คัดลอกโฟลเดอร์ `skills/gridgeist/` ไปยัง Skills directory ของ Agent ตำแหน่งโฟลเดอร์และวิธีตรวจพบ Skill แตกต่างกันในแต่ละผลิตภัณฑ์ หากไม่แน่ใจให้ดูคู่มือ Skills ของ Agent นั้น
3. เปิด Agent session ใหม่ในโปรเจกต์เว็บของคุณ แล้ววาง Prompt นี้:

   ```text
   ใช้ Skill Gridgeist รีวิว Interface นี้โดยยังไม่ต้องแก้โค้ด
   สรุปคำตัดสินหนึ่งบรรทัด ตามด้วยปัญหาที่เรียงตามความสำคัญพร้อมหลักฐาน
   และเสนอทิศทาง Redesign ที่สอดคล้องกันหนึ่งทิศทาง โดยรักษาฟังก์ชันและแบรนด์เดิม
   ```

Agent ที่รองรับการเรียก Skill แบบตรงตัวสามารถใช้ `$gridgeist` ใน Prompt ได้ ดูรายละเอียดเฉพาะผลิตภัณฑ์และตัวอย่างเพิ่มเติมที่ [การติดตั้ง](#การติดตั้ง)

## เหมาะกับงานแบบไหน

- Landing page, Dashboard, Documentation, Portfolio และ Learning platform
- ปรับดีไซน์หน้าเว็บเดิมโดยไม่ทำให้ฟังก์ชันหรือแบรนด์เสีย
- รีวิว Draft และจัดลำดับปัญหาด้าน Hierarchy, Composition, Responsive และ Accessibility
- งานที่ต้องการกลิ่นอาย Swiss, Editorial, Technical minimalism หรือ Visible grid

## การติดตั้ง

### Codex

```powershell
git clone https://github.com/ohmiler/gridgeist.git
Copy-Item -Recurse .\gridgeist\skills\gridgeist "$HOME\.agents\skills\gridgeist"
```

Codex ควรตรวจพบ Skill โดยอัตโนมัติ หากยังไม่ปรากฏ ให้เปิด Codex session ใหม่

สำหรับ Agent อื่นที่รองรับมาตรฐาน `SKILL.md` ให้คัดลอกโฟลเดอร์ `skills/gridgeist/` ไปยัง Skills directory ของ Agent นั้น

### แพ็กเกจ Plugin

Repository นี้เตรียมเป็น Codex Plugin ไว้แล้วผ่าน [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) โดย Plugin จะชี้ไปยังโฟลเดอร์ `skills/gridgeist/` ชุดเดียวกับวิธีติดตั้งตรง ทำให้แก้ไขและดูแล Skill เพียงแหล่งเดียว

เพิ่ม Gridgeist Marketplace แล้วติดตั้ง Plugin ด้วยคำสั่ง:

```powershell
codex plugin marketplace add ohmiler/gridgeist
codex plugin add gridgeist@gridgeist
```

## วิธีเรียกใช้

เรียกใช้โดยตรงด้วย `$gridgeist` แล้วระบุ 4 อย่าง:

1. ผลิตภัณฑ์และกลุ่มผู้ใช้
2. งานที่ต้องการ: สร้างใหม่ ปรับดีไซน์ หรือรีวิว
3. สิ่งที่ต้องรักษา เช่น ฟังก์ชัน สีแบรนด์ หรือเนื้อหา
4. สิ่งที่ต้องตรวจ เช่น Desktop, Mobile, Keyboard และ Accessibility

### Create — สร้างหน้าใหม่

```text
ใช้ $gridgeist ออกแบบ Landing Page สำหรับแพลตฟอร์มเรียน SQL
ให้บทเรียน Query editor และผลลัพธ์เป็นส่วนสำคัญของงานภาพ
หลีกเลี่ยงการ์ด SaaS แบบทั่วไป และตรวจทั้ง Desktop กับ Mobile
```

### Redesign — ปรับดีไซน์เดิม

```text
ใช้ $gridgeist ปรับดีไซน์ Dashboard นี้ใหม่
รักษาฟังก์ชัน เส้นทาง เนื้อหา และสีแบรนด์เดิมทั้งหมด
จัดลำดับข้อมูลตามความสำคัญ และอย่าแก้เพียงแค่ลดความโค้งของการ์ด
```

### Review — รีวิวโดยยังไม่แก้โค้ด

```text
รีวิวหน้าเว็บนี้ด้วย $gridgeist โดยยังไม่ต้องแก้โค้ด
สรุปคำตัดสินหนึ่งบรรทัด ตามด้วยปัญหาที่เรียงตามความสำคัญ
หลักฐาน และทิศทางใหม่ที่สอดคล้องกัน
```

## ทำอย่างไรให้ผลลัพธ์ดีขึ้น

- ให้ Agent ดู Repository และหน้าเว็บที่ Render แล้ว ไม่ใช่แค่คำอธิบาย
- ระบุพฤติกรรมที่ห้ามเปลี่ยนเมื่อทำ Redesign
- ใช้เนื้อหา ข้อมูล โค้ด หรือ Workflow ของผลิตภัณฑ์จริง
- ให้ตรวจหลาย Viewport และสถานะ Interaction
- บอกแบรนด์ที่ต้องรักษา เพื่อไม่ให้ Swiss aesthetic กลายเป็น Preset

## กรณีศึกษา

[Tracefield](https://ohmiler.github.io/tracefield/) คือ Developer Observability Dashboard ที่ใช้ Gridgeist กับโปรเจกต์จริง โดย [Repository](https://github.com/ohmiler/tracefield) เก็บ Baseline, Prompt ที่ใช้, Rubric ประเมินผล, ชุดทดสอบ และ Final interface ไว้ให้ตรวจสอบได้

[Ledgerline](https://ohmiler.github.io/ledgerline/) ทดสอบ Skill เดียวกันกับเว็บไซต์เอกสาร Payment API ที่มีเนื้อหาหนาแน่น โดย [Repository](https://github.com/ohmiler/ledgerline) เก็บ Baseline, Prompt แบบตรงตัว, Rubric 6 ด้าน, เนื้อหา API ที่กำหนดตายตัว, การตรวจ 4 ขนาดหน้าจอ และ Final interface ไว้ครบ

[Morrow](https://ohmiler.github.io/morrow-portfolio/) ทดสอบการปรับตัวตามแบรนด์ด้วย Creative Portfolio แบบ Image-led ที่เป็น Fictional โดย [Repository](https://github.com/ohmiler/morrow-portfolio) เก็บภาพ AI-generated ชุดเดียวกัน, Baseline, Prompt แบบตรงตัว, Rubric 6 ด้าน, การตรวจ 4 ขนาดหน้าจอ และ Final interface ที่ตั้งใจไม่ใช้ภาษาภาพแบบ Technical ของกรณีศึกษาก่อนหน้า

[Doodlewood](https://ohmiler.github.io/doodlewood/) ทดสอบ Playful interaction design ด้วยสตูดิโอวาดรูปสำหรับเด็กแบบ Fictional ที่รักษาความเป็นส่วนตัว โดย [Repository](https://github.com/ohmiler/doodlewood) เก็บ Baseline, Prompt แบบตรงตัว, Rubric 6 ด้าน, Drawing engine ที่ทำงานในเครื่อง, การตรวจ 4 ขนาดหน้าจอ และข้อจำกัดด้านความปลอดภัยของเด็กกับหลักฐานจากผู้ใช้จริงไว้อย่างชัดเจน

กรณีศึกษาที่ทีมสร้างเองทั้ง 4 ตัวจึงครอบคลุมพื้นผิวแบบ Data-heavy, Content-heavy, Image-led และ Playful interactive แล้ว ขั้นต่อไปควรเน้นการตรวจจากผู้ใช้ Agent และโปรเจกต์ภายนอก มากกว่าการเพิ่มหมวดภาพที่ทีมสร้างเองอีก

## ข้อจำกัด

- Gridgeist ให้ทิศทางและกระบวนการ แต่คุณภาพยังขึ้นกับ Context ที่ Agent ได้รับ
- Automated checks ไม่สามารถแทนการตรวจหน้าเว็บจริงได้
- ค่าเริ่มต้นด้าน Grid, Type และสีเป็นเพียงจุดเริ่มต้น ไม่ใช่กฎตายตัว
- ผลลัพธ์จากโมเดลไม่แน่นอน ควรทดสอบซ้ำเมื่อเปลี่ยน Agent หรือแก้ Skill

## การทดสอบ

ชุด Prompt และเกณฑ์ประเมินภาษาไทยอยู่ที่ [`evals/prompts.th.md`](evals/prompts.th.md) ส่วนชุดภาษาอังกฤษอยู่ที่ [`evals/prompts.md`](evals/prompts.md)

## License

[MIT](LICENSE)
