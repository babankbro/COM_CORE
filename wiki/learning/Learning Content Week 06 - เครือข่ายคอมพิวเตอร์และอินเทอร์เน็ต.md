---
type: learning
status: complete
week: 6
source_week: "Week 06 - Computer Networks & Internet"
tags: [learning, week06, en-001-019]
created: "2026-08-03"
updated: "2026-10-12"
---

# Learning Content Week 06: เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต

> ใช้คู่กับ [[Week 06 - Computer Networks & Internet]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

### 1. มองเครือข่ายเป็น "ระบบไปรษณีย์ซ้อนซอง"
ลองนึกถึงการส่งพัสดุข้ามจังหวัด เนื้อหาจดหมายคือ **ข้อมูลของแอป** (เช่น หน้าเว็บ) ชื่อผู้รับ "ห้อง 443" คือ **พอร์ต** ที่บอกว่าข้อมูลเป็นของโปรแกรมใดในเครื่อง บ้านเลขที่คือ **IP address** ที่บอกปลายทางทั้งเส้นทาง ส่วนการส่งต่อระหว่างศูนย์คัดแยกแต่ละแห่งใช้ **MAC address** ซึ่งเปลี่ยนไปทุกช่วง (hop) ศูนย์คัดแยกคือ **router** และสมุดโทรศัพท์ที่แปลงชื่อเป็นบ้านเลขที่คือ **DNS**

ทุกชั้นจะ "ใส่ซองของตัวเองซ้อนทับ" เรียกว่า **encapsulation** ฝั่งผู้รับจะแกะซองย้อนกลับ (**decapsulation**) ชื่อเรียกหน่วยข้อมูลจึงเปลี่ยนไปตามชั้น: Data → Segment → Packet → Frame → Bits การจำชื่อ PDU ให้ถูกช่วยให้อ่านผลจากเครื่องมืออย่าง Wireshark หรือ ping ได้ทันทีว่าปัญหาอยู่ชั้นใด รายละเอียดแต่ละชั้นอ่านต่อที่ [หัวข้อ 1](/module/06/01)

![ภาพเทียบ OSI 7 ชั้นกับ TCP/IP 4 ชั้น ชั้น Application Presentation Session รวมเป็น Application ของ TCP/IP ชั้น Data Link และ Physical รวมเป็น Link พร้อมชื่อ PDU และตัวอย่าง protocol ของแต่ละชั้น](/images/weeks/w06-layer-stack.svg)

### 2. กรณีศึกษาทีละขั้น: พิมพ์ `https://game.example.ac.th` แล้วกด Enter
1. **ตรวจ cache:** เบราว์เซอร์และ OS ดูว่าเคยรู้ IP ของชื่อนี้หรือไม่ ถ้าไม่รู้จึงถาม DNS
2. **DNS:** ส่งคำถามไปยัง DNS resolver (ปกติใช้ UDP พอร์ต 53) ได้คำตอบเป็น IP เช่น `203.0.113.10`
3. **TCP 3-way handshake:** SYN → SYN-ACK → ACK ไปยังพอร์ต 443 เพื่อเปิดช่องทางที่ส่งครบและเรียงลำดับ
4. **TLS handshake:** ตกลงกุญแจเข้ารหัสและตรวจ **certificate** ว่าเป็นเว็บจริง (TLS 1.3 ใช้ 1 รอบไป–กลับ)
5. **HTTP:** ส่ง `GET /` ได้ `200 OK` พร้อม HTML แล้วเบราว์เซอร์จึงดึง CSS, JS และรูปต่อ
6. **Routing:** ระหว่างทาง packet ผ่าน router หลายตัว แต่ละตัวดูเฉพาะ IP ปลายทางเพื่อเลือกเส้นทางถัดไป

ถ้าสมมติ RTT ถึง DNS = 10 ms และถึงเซิร์ฟเวอร์ = 20 ms เวลาก่อนได้ HTML ≈ 10 + 20 + 20 + 20 = **70 ms** ข้อสังเกตคือเวลาส่วนใหญ่หมดไปกับ "การไป–กลับ" ไม่ใช่ขนาดข้อมูล นี่คือเหตุผลที่ HTTP/3 (QUIC บน UDP) และ edge server พยายามลดจำนวนรอบหรือย่นระยะทาง ([หัวข้อ 2](/module/06/02))

![แผนภาพลำดับเวลาเมื่อเปิดเว็บ เริ่มจาก DNS query ไปยัง resolver ตามด้วย TCP handshake TLS handshake และ HTTP GET ไปยัง web server พร้อมแถบเวลารวมประมาณ 70 มิลลิวินาที](/images/weeks/w06-request-journey.svg)

### 3. Private IP, Public IP และ NAT ในชีวิตจริง
เครื่องในหอพักหรือห้องแล็บมักได้ IP แบบ `192.168.x.x` หรือ `10.x.x.x` จาก **DHCP** ซึ่งเป็น **Private IP** ที่บ้านทุกหลังใช้ซ้ำกันได้ router จึงต้องทำ **NAT/PAT** แปลงเป็น Public IP เดียวแล้วจำคู่ "IP:พอร์ตภายใน ↔ พอร์ตภายนอก" ไว้ในตาราง เมื่อคำตอบกลับมาจึงส่งคืนเครื่องได้ถูกตัว ผลข้างเคียงคือคนภายนอกเริ่มเชื่อมต่อเข้าหาเครื่องเราโดยตรงไม่ได้ ถ้าจะเปิดเว็บเซิร์ฟเวอร์ที่บ้านให้คนอื่นเข้าต้องตั้ง **port forwarding** หรือ deploy ขึ้น cloud แทน

ฝึกจำแนก: `10.5.3.2` = Private · `172.20.1.1` = Private (อยู่ในช่วง 172.16–172.31) · `172.32.0.1` = Public · `8.8.8.8` = Public · `127.0.0.1` = loopback (เครื่องตัวเอง)

![ภาพ NAT แสดงเครื่อง PC มือถือ และโน้ตบุ๊กในเครือข่าย 192.168.1.0/24 ส่งข้อมูลผ่าน router ที่แปลงเป็น public IP 203.0.113.5 โดยแยกการเชื่อมต่อด้วยหมายเลขพอร์ต พร้อมขนาดของช่วง private IP ตาม RFC 1918](/images/weeks/w06-nat.svg)

### 4. ตารางเลือกเครื่องมือตามอาการ
| อาการที่พบ | เครื่องมือ | ชั้นที่ตรวจ | ตีความผล |
| :--- | :--- | :--- | :--- |
| ไม่แน่ใจว่าเครื่องได้ IP หรือยัง | `ipconfig /all` / `ip a` | Link–Internet (ค่าในเครื่อง) | ได้ `169.254.x.x` แปลว่าขอ IP จาก DHCP ไม่สำเร็จ |
| เข้าเว็บไม่ได้เลย | `ping 8.8.8.8` | Internet (ICMP) | ping IP ผ่านแต่ ping ชื่อโดเมนไม่ผ่าน → สงสัย DNS |
| ชื่อโดเมนแปลไม่ได้ | `nslookup ชื่อโดเมน` | Application (DNS) | ได้ IP กลับมา = DNS ปกติ |
| เว็บช้ามาก | `tracert` / `traceroute` | Internet (TTL ทีละ hop) | hop ที่เวลากระโดดสูงคือช่วงที่หน่วง |
| เปิดหน้าเว็บได้แต่ API error | เบราว์เซอร์ DevTools / `curl -v` | Application (HTTP) | ดู status code: 4xx ฝั่ง client, 5xx ฝั่ง server |

| ประเด็น | TCP | UDP |
| :--- | :--- | :--- |
| การเชื่อมต่อ | ต้อง handshake ก่อน | ส่งได้ทันที |
| ความครบถ้วน/ลำดับ | รับประกัน (ส่งซ้ำเมื่อหาย) | ไม่รับประกัน |
| overhead และ latency | สูงกว่า | ต่ำกว่า |
| งานที่เหมาะ | เว็บ, อีเมล, โอนไฟล์, API | DNS, เกมออนไลน์, video call, live stream |

### 5. ทำไมวิศวกรต้องสนใจ latency ใน cloud-native และ edge
ใน microservices คำขอหนึ่งครั้งอาจวิ่งต่อกันหลาย service เช่น gateway → auth → order → database ถ้าแต่ละช่วงใช้ 15 ms เวลารวมจะเป็น 4 × 15 = 60 ms ก่อนเริ่มประมวลผลจริงด้วยซ้ำ จึงต้องมี **timeout, retry และ observability** ([หัวข้อ 3](/module/06/03)) ส่วนระบบที่ต้องตอบสนองไวมาก เช่น รถยนต์ที่วิ่ง 120 กม./ชม. (≈ 33.3 ม./วินาที) หากรอคำตอบจาก cloud 100 ms รถจะเคลื่อนไปแล้วราว 3.3 เมตร เหตุนี้ **edge** จึงย้ายการประมวลผลไปใกล้ผู้ใช้ ([หัวข้อ 4](/module/06/04)) และใน [หัวข้อ 5](/module/06/05) จะเห็นว่าอุปกรณ์เครือข่ายเองก็สั่งงานผ่าน API ได้ ซึ่งต่อยอดสู่การสร้าง API ใน [Lab 06](/lab/06)

### สรุปสั้น
- TCP/IP มี 4 ชั้น: Link → Internet → Transport → Application แต่ละชั้นเติม header ของตัวเอง
- PDU: Data → Segment/Datagram → Packet → Frame → Bits
- เปิดเว็บ = DNS → TCP → TLS → HTTP เวลาส่วนใหญ่มาจากจำนวนรอบไป–กลับ (RTT)
- Private IP (RFC 1918) ใช้ซ้ำได้ ออกเน็ตผ่าน NAT ส่วน IPv6 (128 บิต) แก้ปัญหา address ไม่พอ
- เลือกเครื่องมือตามชั้น: ipconfig → ping → nslookup → tracert → curl
- TCP = ครบและเรียง, UDP = เร็วและเบา เลือกตามความต้องการของงาน

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

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 6: [[Week 06 - Computer Networks & Internet]]
