ยินดีต้อนรับเข้าสู่สัปดาห์ที่ 12 ในสัปดาห์นี้เราจะมุ่งเน้นไปที่หัวใจสำคัญของวิศวกรรมคอมพิวเตอร์ในยุคปัจจุบัน นั่นคือ **"ความมั่นคงปลอดภัยทางไซเบอร์ (Cybersecurity)"** และ **"สถาปัตยกรรมความน่าเชื่อถือ (Trust Architecture)"** 

เมื่อระบบซอฟต์แวร์และฮาร์ดแวร์มีการเชื่อมต่อถึงกันมากขึ้น ความเสี่ยงที่จะถูกโจมตี ขโมยข้อมูล หรือทำลายระบบก็เพิ่มสูงขึ้นเป็นเงาตามตัว การสร้างระบบที่ใช้งานได้ดีเพียงอย่างเดียวจึงไม่เพียงพอ วิศวกรคอมพิวเตอร์จะต้องมีความสามารถในการออกแบบระบบให้มีความทนทานต่อภัยคุกคาม และปกป้องข้อมูลผู้ใช้งานได้อย่างมีประสิทธิภาพ

## วัตถุประสงค์การเรียนรู้ของสัปดาห์นี้
ผู้เรียนจะได้ทำความเข้าใจในประเด็นสำคัญดังต่อไปนี้:
1. **หลักความปลอดภัยและ CIA Triad:** เข้าใจพื้นฐานของการรักษาความลับ (Confidentiality), ความถูกต้องสมบูรณ์ (Integrity), และความพร้อมใช้งาน (Availability)
2. **วิทยาการรหัสลับเบื้องต้น (Cryptography):** เรียนรู้กลไกการเข้ารหัสข้อมูลทั้งแบบสมมาตร (Symmetric) และอสมมาตร (Asymmetric) รวมถึงการประยุกต์ใช้งาน
3. **ภัยคุกคามทางไซเบอร์ (Cyber Threats):** รู้จักรูปแบบการโจมตีที่พบบ่อยในปัจจุบัน และแนวทางการป้องกันระดับเครือข่ายและระบบ
4. **สถาปัตยกรรม Zero Trust:** เปลี่ยนผ่านจากแนวคิดการรักษาความปลอดภัยแบบดั้งเดิม สู่กระบวนทัศน์ใหม่ที่ยึดหลัก "Never trust, always verify"
5. **Digital Provenance และ AI Deepfakes:** เข้าใจความท้าทายใหม่ที่เกิดจาก Generative AI และแนวทางการรับรองแหล่งที่มาของสื่อดิจิทัล

การเรียนรู้ในสัปดาห์นี้จะปูพื้นฐานที่แข็งแกร่งให้นักศึกษาสามารถนำแนวคิดด้าน Security-by-Design ไปประยุกต์ใช้ในการพัฒนาซอฟต์แวร์และสถาปัตยกรรมระบบในโลกการทำงานจริงได้อย่างมืออาชีพ

---


## คำถามนำ
เราจะปกป้องระบบที่กระจายบน cloud, IoT และ AI ได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบาย CIA triad และ threat พื้นฐาน
2. เข้าใจ least privilege, MFA, encryption และ secure coding
3. อธิบาย Zero Trust และ OWASP Top 10

## แก่นความรู้ที่ต้องเข้าใจ
- CIA triad คือ confidentiality, integrity, availability เป็นกรอบแรกในการคิดความปลอดภัย
- Zero Trust ย้ายจากการเชื่อใจเครือข่ายภายใน ไปสู่การตรวจสอบ identity, device, context และ policy ทุกครั้ง
- OWASP Top 10 เป็นเอกสาร awareness สำหรับความเสี่ยงเว็บแอปที่นักพัฒนาควรรู้

## เนื้อหาเรียนรู้
- เริ่มจาก incident สมมุติ เช่นเว็บแอปถูก SQL injection แล้วให้ผู้เรียนแยกว่า CIA ด้านใดเสียหายและควรป้องกันที่ชั้นใด
- อธิบาย defense-in-depth: ไม่มีมาตรการเดียวพอ ต้องรวม authentication, authorization, encryption, logging, backup และ patching
- NIST SP 800-207 ช่วยให้สอน Zero Trust เป็นสถาปัตยกรรม ไม่ใช่ผลิตภัณฑ์: ทุก request ต้องประเมินความเสี่ยงตาม policy ก่อนให้เข้าถึง resource

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

ส่วนนี้ต่อยอดจากหัวข้อเจาะลึก ([หัวข้อ 1](/module/12/01) ถึง [หัวข้อ 5](/module/12/05)) ด้วยภาพเปรียบเทียบในชีวิตประจำวัน และวิเคราะห์ incident สมมุติของโครงงาน IoT dashboard ทีละขั้น เพื่อใช้ทำ threat model ใน [Lab 12](/lab/12)

### 1. CIA triad ในภาษาชีวิตประจำวัน

- **Confidentiality (ความลับ)** เหมือน "ซองจดหมายปิดผนึก" มีแต่ผู้มีสิทธิ์เท่านั้นที่อ่านได้ เครื่องมือหลักคือการเข้ารหัส การควบคุมสิทธิ์ และ MFA
- **Integrity (ความถูกต้องสมบูรณ์)** เหมือน "ตราประทับครั่ง" ถ้ามีใครแกะหรือแก้ไข ผู้รับต้องรู้ได้ เครื่องมือหลักคือ hash, HMAC และ digital signature
- **Availability (ความพร้อมใช้งาน)** เหมือน "ร้านสะดวกซื้อที่เปิด 24 ชั่วโมง" ข้อมูลถูกต้องและเป็นความลับก็ไร้ค่าถ้าเรียกใช้ไม่ได้ เครื่องมือหลักคือ redundancy, backup และการป้องกัน DDoS

![แผนภาพสามเหลี่ยม CIA triad มีมุม Confidentiality, Integrity และ Availability แต่ละมุมมีการ์ดแสดงตัวอย่างภัยคุกคามและมาตรการป้องกัน พร้อมขั้นตอนการใช้กรอบนี้วิเคราะห์เหตุการณ์](/images/weeks/w12-cia-triad.svg)

ดูนิยามฉบับย่อได้ที่ [CIA Triad](/concept/cia-triad) ข้อสังเกตคือสามด้านนี้มักดึงกันเอง เช่น ล็อกระบบแน่นหนาเกินไป (C สูง) จนผู้ใช้ที่ถูกต้องเข้าไม่ได้ (A ต่ำ) วิศวกรจึงต้องหาจุดสมดุลตามความเสี่ยงของ asset นั้น

### 2. Defense-in-depth: แผ่นชีสสวิสหลายแผ่น

แบบจำลอง Swiss cheese ของ James Reason อธิบายว่ามาตรการทุกชั้นมี "รู" (จุดอ่อน) เสมอ เช่น ผู้ใช้หลงเชื่อ phishing หรือมี patch ที่ยังไม่ได้ติดตั้ง ความเสียหายจะเกิดเมื่อรูของทุกแผ่นเรียงตรงกันพอดี การซ้อนหลายชั้น (identity, application, data, network, monitoring, backup) จึงลดโอกาสที่ช่องโหว่เดียวจะลามเป็นหายนะ

### 3. ตัวอย่าง incident: IoT dashboard ของโครงงานถูกเจาะ

**สถานการณ์สมมุติ:** ทีมทำเว็บ dashboard ที่อ่านค่าจาก MQTT broker หน้า login สร้าง SQL ด้วยการต่อ string รหัสผ่านเก็บเป็น MD5 แบบไม่มี salt และใช้ username/password ชุดเดียวกันทั้งเว็บและ broker ซึ่งไม่ได้ตั้ง ACL ราย topic

| ขั้น | ผู้โจมตีทำอะไร | CIA ที่เสีย | control ที่ควรหยุดได้ (ชั้น) |
|---|---|---|---|
| 1 | ใส่ `' OR '1'='1` ในช่อง login แล้วดึงตาราง users (OWASP Top 10:2021 A03 Injection) | C | parameterized query + least privilege ของบัญชีฐานข้อมูล (application) |
| 2 | crack hash MD5 ไม่มี salt ด้วย GPU หรือ rainbow table ได้รหัสผ่านจริงในเวลาสั้น | C | เก็บรหัสผ่านด้วย Argon2id หรือ bcrypt ที่มี salt (data) |
| 3 | นำรหัสเดิมไป login broker (credential reuse) | C, I | MFA สำหรับผู้ดูแล + credential แยกรายอุปกรณ์ (identity) |
| 4 | publish ค่าอุณหภูมิปลอม 15 °C ไปที่ `building5/EN301/temperature` ทำให้ระบบสั่งปิดแอร์ผิด | I | ACL ราย topic + TLS + ตรวจช่วงค่าที่สมเหตุสมผล (network/application) |
| 5 | ยิงข้อความหลายพันต่อวินาทีจน broker ล่ม | A | rate limit, จำกัดจำนวน connection, แจ้งเตือนจาก log (monitoring) |
| 6 | ทีมกู้ระบบ | A | backup ที่ทดสอบการกู้คืนแล้ว + แผนรับมือ incident (recovery) |

เมื่อเทียบกับฟังก์ชันของ NIST Cybersecurity Framework 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) จะเห็นว่าทีมนี้มีปัญหาตั้งแต่ Identify (ไม่ได้ทำ threat model) และไม่มีชั้น Detect เลย จึงรู้ตัวเมื่อระบบล่มไปแล้ว

### 4. Cryptography แบบเห็นภาพ: กุญแจบ้าน ตู้ไปรษณีย์ และลายนิ้วมือ

![แผนภาพเปรียบเทียบการเข้ารหัส symmetric ที่ใช้กุญแจลับ K ดอกเดียวกันทั้งสองฝั่ง กับ asymmetric ที่เข้ารหัสด้วย public key ของ Bob และถอดรหัสด้วย private key ของ Bob พร้อมสรุปว่า TLS ใช้ทั้งสองแบบร่วมกัน](/images/weeks/w12-crypto-keys.svg)

- **Symmetric (AES)** เหมือน "กุญแจบ้านที่ปั๊มให้คนในบ้าน" ใช้ดอกเดียวกันทั้งล็อกและเปิด เร็วมาก แต่ปัญหาคือจะส่งกุญแจให้อีกฝ่ายอย่างปลอดภัยได้อย่างไร
- **Asymmetric (RSA, ECC)** เหมือน "ตู้ไปรษณีย์หน้าบ้าน" ใครก็หย่อนจดหมายได้ (public key) แต่เจ้าของบ้านคนเดียวที่มีกุญแจเปิด (private key)
- **Hash (SHA-256)** เหมือน "ลายนิ้วมือของข้อมูล" ได้ผลลัพธ์ยาวคงที่ 256 bit (64 ตัวอักษร hex) เปลี่ยนข้อมูลเพียง 1 ตัวอักษร ลายนิ้วมือจะเปลี่ยนทั้งหมด และย้อนกลับเป็นข้อมูลเดิมไม่ได้
- **รหัสผ่านต้อง "hash" ไม่ใช่ "encrypt"** และต้องใช้ฟังก์ชันที่ออกแบบให้ช้าและมี salt เช่น Argon2id หรือ bcrypt ตามคำแนะนำของ OWASP Password Storage Cheat Sheet เพราะ SHA-256 เปล่า ๆ เร็วเกินไปจนเดารหัสได้หลายพันล้านครั้งต่อวินาทีบน GPU

### 5. Perimeter กับ Zero Trust: ปราสาทกับสนามบิน

แบบเดิมเหมือน **ปราสาทที่มีคูน้ำ** ข้ามสะพานเข้ามาได้ครั้งเดียวก็เดินไปได้ทุกห้อง ส่วน Zero Trust เหมือน **สนามบินหรือโรงแรมที่ใช้คีย์การ์ด** ต้องแสดงตัวที่ทุกด่าน และบัตรเปิดได้เฉพาะห้องของตัวเอง ([Zero-Trust Architecture](/concept/zero-trust-architecture), [หัวข้อ 4](/module/12/04))

![แผนภาพเปรียบเทียบ perimeter security ที่ผู้โจมตีผ่าน firewall ครั้งเดียวแล้วเคลื่อนที่ไปทั่วเครือข่ายภายใน กับ Zero Trust ที่ทุก request ของผู้ใช้และอุปกรณ์ต้องผ่าน PEP ซึ่งถาม PDP โดยใช้สัญญาณ identity, สภาพอุปกรณ์ และบริบท ก่อนเข้าถึง resource ทีละรายการ](/images/weeks/w12-zero-trust.svg)

| ประเด็น | Perimeter (castle-and-moat) | Zero Trust (NIST SP 800-207) |
|---|---|---|
| สมมติฐาน | ภายในเครือข่าย = เชื่อใจได้ | ไม่เชื่อใจโดยปริยาย ไม่ว่าอยู่ภายในหรือภายนอก |
| จุดตรวจ | firewall/VPN ที่ขอบเครือข่ายครั้งเดียว | PEP หน้าทุก resource ตัดสินโดย PDP ทุก session |
| หลักฐานที่ใช้ | IP หรือการอยู่ใน LAN | identity + MFA, สภาพอุปกรณ์, บริบท, พฤติกรรม |
| เมื่อถูกเจาะ 1 เครื่อง | ลามไปเครื่องอื่นได้ง่าย (lateral movement) | ถูกจำกัดด้วย micro-segmentation และ least privilege |
| เหมาะกับ | ระบบที่อยู่ในสำนักงานเดียว | cloud, ทำงานจากที่ไหนก็ได้, IoT จำนวนมาก |

### สรุปสั้น

- วิเคราะห์ทุก incident ด้วยคำถาม "C, I หรือ A เสีย" แล้วเลือก control ให้ตรงด้าน หนึ่งเหตุการณ์อาจกระทบหลายด้าน
- Defense-in-depth: ไม่มีมาตรการใดไร้รู ต้องซ้อนหลายชั้นตั้งแต่ identity ถึง backup
- SQL injection ป้องกันด้วย parameterized query ไม่ใช่การกรองตัวอักษรด้วยมือ
- Symmetric เร็วแต่มีปัญหาแจกกุญแจ asymmetric แก้ปัญหานี้ได้แต่ช้า TLS จึงใช้ร่วมกัน
- รหัสผ่านเก็บด้วย slow hash + salt (Argon2id, bcrypt) ห้ามเก็บแบบ plaintext, MD5 หรือ encrypt
- Zero Trust = never trust, always verify ตรวจ identity, อุปกรณ์ และบริบททุก request ด้วย PDP/PEP

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ให้ผู้เรียนทำ threat model ของ IoT dashboard ในโครงงาน แล้วกำหนด control อย่างน้อย 5 รายการ

## คำถามตรวจความเข้าใจ
1. CIA triad แต่ละข้อมีตัวอย่างอะไร?
2. Zero Trust ต่างจาก perimeter security อย่างไร?
3. OWASP Top 10 ช่วยนักพัฒนาอย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Zero Trust, OWASP และ secure design

- NIST SP 800-207 อธิบาย Zero Trust เป็นสถาปัตยกรรมที่ย้ายจุดเน้นจาก network perimeter ไปที่ users, assets และ resources
- OWASP Top 10 เป็น awareness baseline สำหรับนักพัฒนาเว็บ และควรโยงกับ secure coding เช่น access control, injection และ cryptographic failures
- สำหรับระบบ AI/IoT ควรเพิ่ม OWASP LLM risks และ device security เพราะ attack surface ขยายจากเว็บไปยัง prompt, model, vector store และ sensor/device

**แหล่งอ้างอิงข้อมูล:**
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> ความปลอดภัยไซเบอร์มุ่งปกป้องระบบ/ข้อมูลตามหลัก [CIA Triad](/concept/cia-triad) ภัยคุกคามปัจจุบันรุนแรงขึ้นและถูกขับเคลื่อนด้วย AI ทั้งฝ่ายโจมตีและฝ่ายป้องกัน แนวทาง [Zero-Trust Architecture](/concept/zero-trust-architecture) เป็นมาตรฐานใหม่

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจหลักการพื้นฐานด้านความปลอดภัยไซเบอร์ ([CIA Triad](/concept/cia-triad)) — *CLO1*
2. ผู้เรียนเข้าใจสถาปัตยกรรม [Zero-Trust Architecture](/concept/zero-trust-architecture) ในองค์กรยุคใหม่ — *CLO1*
3. ผู้เรียนตระหนักถึง Digital Provenance เพื่อตรวจสอบที่มาของข้อมูลในยุคที่ AI สร้างเนื้อหาปลอมได้ — *CLO4*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- หลักความปลอดภัย ([CIA Triad](/concept/cia-triad): Confidentiality, Integrity, Availability)
- วิทยาการรหัสลับเบื้องต้น (Cryptography)
- [Zero-Trust Architecture](/concept/zero-trust-architecture): "ไม่เชื่อใจใคร ตรวจสอบทุกครั้ง"
- Digital Provenance & Watermarking: ตรวจสอบสื่อ/ซอฟต์แวร์ที่สร้างโดย AI (Deepfakes)

### 📖 เนื้อหาโดยละเอียด
- **หลักการ:** [CIA Triad](/concept/cia-triad), least privilege, defense in depth
- **ภัยคุกคาม:** มัลแวร์/แรนซัมแวร์, ฟิชชิง, social engineering, DDoS, SQL injection, MITM
- **กลไกป้องกัน:** การเข้ารหัส, MFA/2FA, ไฟร์วอลล์, IDS/IPS, การสำรองข้อมูล, IAM, patching
- **กรอบมาตรฐาน:** NIST CSF, ISO/IEC 27001, **OWASP Top 10**

### 🔑 แนวคิดหลัก (Key Concepts)
[CIA Triad](/concept/cia-triad) · [Zero-Trust Architecture](/concept/zero-trust-architecture) · ดูธีม [ความปลอดภัยและสถาปัตยกรรมความน่าเชื่อถือ (ธีม)](/docs/theme-security)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **ภัยที่ขับเคลื่อนด้วย AI:** ~87% ระบุว่าช่องโหว่ที่เกี่ยวกับ AI โตเร็วที่สุดในปี 2025
- **แรนซัมแวร์ยังครองอันดับ:** double-extortion (ขโมย+เข้ารหัส) เป็นมาตรฐาน
- **[Zero-Trust Architecture](/concept/zero-trust-architecture) เป็นกระแสหลัก:** ~96% ขององค์กรสนับสนุน
- **OWASP Top 10 for LLM:** เพิ่มความเสี่ยงเฉพาะ AI เช่น prompt injection, vector/embedding weaknesses (เชื่อม [สัปดาห์ที่ 10: Generative AI & Modern Robotics](/module/10))

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 9
Lab 1 ชม. (เทคนิคเข้ารหัสผ่าน/ความปลอดภัย) + Project 1 ชม. (ประยุกต์ใช้ความปลอดภัยในระบบ IoT + นำเสนอ) — **Module 3: IoT & Smart Systems**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. อธิบาย CIA triad พร้อมตัวอย่างการละเมิดแต่ละด้าน
2. Zero Trust ต่างจากการป้องกันแบบ "ขอบเขตเครือข่าย" เดิมอย่างไร
3. ยกความเสี่ยงใน OWASP Top 10 for LLM มา 2 ข้อ

### 📚 อ้างอิง (References)
- Stallings, W. (2022). *Cryptography and Network Security* (8th ed.). Pearson.
- NIST. *SP 800-207, Zero Trust Architecture.*
- World Economic Forum. *Global Cybersecurity Outlook 2026.* [reports.weforum.org](https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2026.pdf)
- OWASP Foundation. *OWASP Top 10 & Top 10 for LLM.* [owasp.org](https://owasp.org/)
- Trend Micro. *2025 Cyber Risk Report.* [trendmicro.com](https://www.trendmicro.com/vinfo/us/security/news/threat-landscape/trend-2025-cyber-risk-report)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. หลักความปลอดภัยและ CIA Triad](/module/12/01)
- [02. วิทยาการรหัสลับเบื้องต้น Cryptography](/module/12/02)
- [03. ภัยคุกคามทางไซเบอร์และการป้องกัน](/module/12/03)
- [04. สถาปัตยกรรม Zero Trust](/module/12/04)
- [05. Digital Provenance และ AI Deepfakes](/module/12/05)
