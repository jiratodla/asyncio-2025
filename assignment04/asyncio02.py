# Create 1 Task with High-Level API
import asyncio
async def do_someting():
    print("เริ่มทำงาน...")
    await asyncio.sleep(2)
    print("ทำงานเสร็จแล้ว!")

async def main():
        task = asyncio.create_task(do_someting())
        await task

asyncio.run(main())