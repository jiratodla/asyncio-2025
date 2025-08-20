# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. ..Task ถูกสร้างขึ้นและ รันต่อไป
   2. ..เมื่อจบ(main)และ asyncio.run(main())ปิด event loop ถ้ายังมีtaskที่ยังไม่เสร็จแาจจะถูกยกเลิก
   3. ..จะไม่เห็นค่าผลลัพธ์และไม่เห็นError
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. ..gather จะส่งค่าออกตามลำดับที่ค่าเข้ามา wait คืนค่าเป็น(Done,pending)
   2. ..gather จะรอเสร็จทุกtaskแล้วค่อยส่งค่าออก wait เลือกได้ว่าจะเอาค่าไหน
   3. ..gather โยน exception ของ task แรกที่ error wait ต้องเช็คจาก task เอง
3. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. ..coroutine เริ่มตอนถึงบรรทัด await	  create_taskเริ่มทันทีที่เรียก create_task
   2. ..coroutine จะต้องรอผลลัพธ์้สมอ await	  create_taskไม่จำเป็นต้องรอผลลัพธ์ทันที
   3. ..coroutine ความสามารถในการจัดการหลายtaskลำบากมากว่า  create_task ง่ายเพราะ เก็บreference task แล้วรอพร้อมกัน
