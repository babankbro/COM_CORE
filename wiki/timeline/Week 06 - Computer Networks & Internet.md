---
type: chapter
status: complete
week: 6
clo: [CLO1]
tags: [curriculum, week06, network, internet, tcp-ip, 5g, cloud]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 6: เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต

> [!abstract] สาระสำคัญ
> เครือข่ายเชื่อมอุปกรณ์ให้สื่อสาร/แบ่งปันทรัพยากร อินเทอร์เน็ตคือ "เครือข่ายของเครือข่าย" ที่ทำงานบนชุดโพรโทคอล [[TCP-IP Model|TCP/IP]]

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนอธิบายสถาปัตยกรรมและโปรโตคอลพื้นฐานของเครือข่าย/อินเทอร์เน็ตได้ — *CLO1*
2. ผู้เรียนเข้าใจการออกแบบเครือข่ายสำหรับระบบ Cloud-native — *CLO1*
3. ผู้เรียนตระหนักถึงบทบาทของ [[Edge Computing|Edge Networks]] ในการลดความหน่วง (Latency) — *CLO1*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- สถาปัตยกรรมเครือข่ายพื้นฐาน, OSI และ [[TCP-IP Model]]
- โปรโตคอลอินเทอร์เน็ตและการสื่อสารสมัยใหม่ (5G/6G, Wi-Fi 7)
- เครือข่ายสำหรับ Cloud-native และ Microservices
- Edge Networks สำหรับระบบตอบสนองไว (Real-time)

## 📖 เนื้อหาโดยละเอียด
- **ประเภทเครือข่าย:** LAN, WAN, MAN, PAN; มีสาย/ไร้สาย
- **แบบจำลองอ้างอิง:** OSI 7 ชั้น และ [[TCP-IP Model]] 4 ชั้น
- **โพรโทคอล:** IP (IPv4/IPv6), TCP/UDP, HTTP/HTTPS, DNS, DHCP
- **อุปกรณ์:** switch, router, access point; addressing & subnet
- **คลาวด์:** IaaS/PaaS/SaaS เชื่อม [[Week 07 - Data Center & Cloud Infrastructure]]

## 🔑 แนวคิดหลัก (Key Concepts)
[[TCP-IP Model]] · [[Edge Computing]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Wi‑Fi 7 (802.11be)** เริ่มวางตลาดจริงกลางปี 2025 ความเร็วหลายกิกะบิต หน่วงต่ำ
- **5G‑Advanced → 6G:** 6G ตั้งเป้าความเร็วระดับ Tbps; เริ่มกระบวนการมาตรฐาน
- **AI ในเครือข่าย + SDN/NFV:** บริหารเครือข่ายอัตโนมัติตลอดวงจรชีวิต
- **ดาวเทียม LEO + ไฮบริด:** ขยายการเข้าถึงพื้นที่ห่างไกล

## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 6
Lab 1 ชม. (Network simulation/Ping) + Project 1 ชม. (สร้าง API และ Web Router) — **Module 2: Web Dev**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]

## ❓ คำถามทบทวน
1. TCP กับ UDP ต่างกันอย่างไร เหมาะกับงานใด
2. DNS ทำหน้าที่อะไร
3. IaaS, PaaS, SaaS ต่างกันอย่างไร

## 📚 อ้างอิง (References)
- Kurose, J. F., & Ross, K. W. (2021). *Computer Networking: A Top-Down Approach* (8th ed.). Pearson.
- ACM/IEEE-CS CC2020 — Networking and Communication (NC).
- IEEE SA. *Six Connectivity and Telecom Trends to Watch for in 2025.* [standards.ieee.org](https://standards.ieee.org/beyond-standards/2025-connectivity-telecom-trends/)
- TS2. *Global Next-Gen Networking Developments 2025: 5G, 6G & Wi‑Fi 7.* [ts2.tech](https://ts2.tech/en/global-next-gen-networking-developments-june-july-2025-5g-6g-wi%E2%80%91fi-7-news-roundup/)

## 🔗 นำทาง
⬅️ [[Week 05 - Database & Data Management]] · ➡️ [[Week 07 - Data Center & Cloud Infrastructure]]
