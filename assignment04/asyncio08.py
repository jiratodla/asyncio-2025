# get Exception
import asyncio

async def erroe_task():
    await asyncio.sleep(1)
    raise ValueError("เกิดข้อผิดพลาด")

async def main():
    task = asyncio.create_task(erroe_task())
    try:
        await task
    except Exception:
        print("Exception ที่เกิด:", task.exception())

asyncio.run(main())