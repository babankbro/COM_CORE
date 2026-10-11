## Definition
บัสสื่อสารอนุกรมแบบ synchronous ที่ใช้สายเพียง 2 เส้น คือ **SDA** (ข้อมูล) และ **SCL** (สัญญาณนาฬิกา) โดย **controller** (เช่น ESP32) เป็นผู้สร้าง clock และเริ่มการสื่อสาร ส่วน **target** (เช่น เซนเซอร์) ตอบเมื่อถูกเรียกด้วย address 7 บิตของตัวเอง ทำให้ต่ออุปกรณ์หลายตัวบนสายคู่เดียวกันได้ ความเร็วทั่วไปคือ 100 kHz (Standard mode) และ 400 kHz (Fast mode)

## Course Context
- ใช้ใน [สัปดาห์ที่ 11: Embedded Systems & IoT](/module/11) สำหรับอ่านเซนเซอร์บนบอร์ด ESP32/KidBright32 ด้วย MicroPython: `I2C(...)`, `i2c.scan()`, `i2c.readfrom_mem(addr, reg, nbytes)`
- ตัวอย่างปฏิบัติ (VEML6075 ที่ address `0x10`, การรวมไบต์ little-endian) ดูที่ [Lab 11 - MQTT Data Transmission](/lab/11)
- เกี่ยวข้องกับ [Edge Computing](/concept/edge-computing) เพราะเป็นช่องทางนำข้อมูลจากเซนเซอร์เข้าสู่อุปกรณ์ปลายทาง

## อ้างอิง
- NXP, *UM10204: I2C-bus specification and user manual* https://www.nxp.com/docs/en/user-guide/UM10204.pdf
- MicroPython docs: `machine.I2C` https://docs.micropython.org/en/latest/library/machine.I2C.html
