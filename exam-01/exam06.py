# Hint:
# ปัญหา: asyncio.gather() จะ throw ข้อผิดพลาดทั้งหมด ไม่ใช่แค่ตัวแรก
# ให้แก้ไขโค้ดเพื่อให้สามารถ จัดการข้อผิดพลาดแยกแต่ละ task ได้
# Result:
# [ValueError('Something went wrong!'), ValueError('Something went wrong!')]

import asyncio

async def risky_task():
    raise ValueError("Something went wrong!")

async def main():
    tasks = []
    for _ in range(2):
        tasks.append(asyncio.create_task(risky_task()))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    print(results)        
asyncio.run(main())
