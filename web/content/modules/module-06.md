## คำถามนำ
ข้อมูลเดินทางจากเครื่องเราไปยังบริการบนอินเทอร์เน็ตผ่านชั้นใดบ้าง?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบาย OSI/TCP-IP model
2. รู้จัก IP, TCP/UDP, DNS, HTTP/HTTPS และ subnet
3. เข้าใจ latency, edge network และ cloud-native networking

## แก่นความรู้ที่ต้องเข้าใจ
- TCP/IP เป็นกรอบคิดหลักของอินเทอร์เน็ต แบ่งบทบาทตั้งแต่ link, internet, transport ถึง application
- TCP เน้นความครบถ้วนและลำดับข้อมูล ส่วน UDP ลด overhead เหมาะกับงาน real-time บางประเภท
- IPv6 ตาม RFC 8200 เป็นมาตรฐานสำคัญสำหรับพื้นที่ address และการเติบโตของอินเทอร์เน็ต

## เนื้อหาเรียนรู้
- สอนด้วยการเปิดเว็บหนึ่งหน้า: DNS แปลงชื่อโดเมนเป็น IP, TCP/TLS สร้างการเชื่อมต่อ, HTTP ส่ง request/response, router ส่ง packet ผ่านหลายเครือข่าย
- ให้ผู้เรียนเห็นว่าเครือข่ายไม่ใช่แค่สายหรือ Wi-Fi แต่รวม protocol, addressing, routing, security และ performance
- โยง cloud-native: microservices จำนวนมากต้องสื่อสารกันผ่าน network ภายใน cluster ดังนั้น latency, retry, timeout และ observability กลายเป็นหัวข้อวิศวกรรมสำคัญ

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ใช้ ping, tracert/traceroute และ nslookup ตรวจเส้นทางไปยังเว็บหนึ่ง แล้วอธิบายผลด้วย TCP/IP model

## คำถามตรวจความเข้าใจ
1. DNS ทำหน้าที่อะไร?
2. TCP กับ UDP ต่างกันอย่างไร?
3. IPv6 แก้ข้อจำกัดสำคัญใดของ IPv4?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Internet standards, Wi-Fi 7 และ 5G-Advanced

- IETF RFC 8200 เป็นแหล่งหลักสำหรับ IPv6 ใช้สอนว่ามาตรฐานอินเทอร์เน็ตเกิดจาก consensus และ interoperability
- IEEE 802.11be-2024 หรือ Wi-Fi 7 เพิ่มเป้าหมาย throughput สูงมากและปรับ PHY/MAC เพื่อรองรับงาน latency ต่ำ เหมาะเชื่อมกับ real-time/edge applications
- 3GPP Release 18 เป็นจุดเริ่มของ 5G-Advanced มีแนวทางใช้ AI/ML ในเครือข่ายและเพิ่มความสามารถของ mobile network

**แหล่งอ้างอิงข้อมูล:**
- [IETF RFC 8200: IPv6 Specification](https://datatracker.ietf.org/doc/html/rfc8200)
- [IEEE 802.11be-2024](https://standards.ieee.org/ieee/802.11be/7516/)
- [3GPP Release 18 overview](https://www.3gpp.org/specifications-technologies/releases/release-18)

## แหล่งค้นคว้าเพิ่มเติม
- [IETF RFC 8200 IPv6 Specification](https://datatracker.ietf.org/doc/html/rfc8200)
- [Cloud Native Computing Foundation](https://www.cncf.io/)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> เครือข่ายเชื่อมอุปกรณ์ให้สื่อสาร/แบ่งปันทรัพยากร อินเทอร์เน็ตคือ "เครือข่ายของเครือข่าย" ที่ทำงานบนชุดโพรโทคอล [TCP/IP](/concept/tcp-ip-model)

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนอธิบายสถาปัตยกรรมและโปรโตคอลพื้นฐานของเครือข่าย/อินเทอร์เน็ตได้ — *CLO1*
2. ผู้เรียนเข้าใจการออกแบบเครือข่ายสำหรับระบบ Cloud-native — *CLO1*
3. ผู้เรียนตระหนักถึงบทบาทของ [Edge Networks](/concept/edge-computing) ในการลดความหน่วง (Latency) — *CLO1*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- สถาปัตยกรรมเครือข่ายพื้นฐาน, OSI และ [TCP-IP Model](/concept/tcp-ip-model)
- โปรโตคอลอินเทอร์เน็ตและการสื่อสารสมัยใหม่ (5G/6G, Wi-Fi 7)
- เครือข่ายสำหรับ Cloud-native และ Microservices
- Edge Networks สำหรับระบบตอบสนองไว (Real-time)

### 📖 เนื้อหาโดยละเอียด
- **ประเภทเครือข่าย:** LAN, WAN, MAN, PAN; มีสาย/ไร้สาย
- **แบบจำลองอ้างอิง:** OSI 7 ชั้น และ [TCP-IP Model](/concept/tcp-ip-model) 4 ชั้น
- **โพรโทคอล:** IP (IPv4/IPv6), TCP/UDP, HTTP/HTTPS, DNS, DHCP
- **อุปกรณ์:** switch, router, access point; addressing & subnet
- **คลาวด์:** IaaS/PaaS/SaaS เชื่อม [สัปดาห์ที่ 7: Data Center & Cloud Infrastructure](/module/07)

### 🔑 แนวคิดหลัก (Key Concepts)
[TCP-IP Model](/concept/tcp-ip-model) · [Edge Computing](/concept/edge-computing)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Wi‑Fi 7 (802.11be)** เริ่มวางตลาดจริงกลางปี 2025 ความเร็วหลายกิกะบิต หน่วงต่ำ
- **5G‑Advanced → 6G:** 6G ตั้งเป้าความเร็วระดับ Tbps; เริ่มกระบวนการมาตรฐาน
- **AI ในเครือข่าย + SDN/NFV:** บริหารเครือข่ายอัตโนมัติตลอดวงจรชีวิต
- **ดาวเทียม LEO + ไฮบริด:** ขยายการเข้าถึงพื้นที่ห่างไกล

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 6
Lab 1 ชม. (Network simulation/Ping) + Project 1 ชม. (สร้าง API และ Web Router) — **Module 2: Web Dev**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. TCP กับ UDP ต่างกันอย่างไร เหมาะกับงานใด
2. DNS ทำหน้าที่อะไร
3. IaaS, PaaS, SaaS ต่างกันอย่างไร

### 📚 อ้างอิง (References)
- Kurose, J. F., & Ross, K. W. (2021). *Computer Networking: A Top-Down Approach* (8th ed.). Pearson.
- ACM/IEEE-CS CC2020 — Networking and Communication (NC).
- IEEE SA. *Six Connectivity and Telecom Trends to Watch for in 2025.* [standards.ieee.org](https://standards.ieee.org/beyond-standards/2025-connectivity-telecom-trends/)
- TS2. *Global Next-Gen Networking Developments 2025: 5G, 6G & Wi‑Fi 7.* [ts2.tech](https://ts2.tech/en/global-next-gen-networking-developments-june-july-2025-5g-6g-wi%E2%80%91fi-7-news-roundup/)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. สถาปัตยกรรมเครือข่ายพื้นฐาน OSI และ TCP IP Model](/module/06/01)
- [02. โปรโตคอลอินเทอร์เน็ตและการสื่อสารสมัยใหม่](/module/06/02)
- [03. เครือข่ายสำหรับ Cloud native และ Microservices](/module/06/03)
- [04. Edge Networks สำหรับระบบตอบสนองไว](/module/06/04)
- [05. การจำลองเครือข่ายและระบบ API เบื้องต้น](/module/06/05)
