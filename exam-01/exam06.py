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
    try:
        
        asyncio.gather(risky_task(), risky_task())
        await asyncio.sleep(1)

        
    except Exception as e:
        print("Caught:", e)
    print([t.exception() for t in tasks])
        
asyncio.run(main())
