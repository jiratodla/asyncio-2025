# Hint:
# ให้หาข้อผิดพลาดและแก้ไขโค้ดให้ทำงานถูกต้อง
# Result:
# Hello
# World

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    task = asyncio.create_task(say_hello())  # สร้าง task แล้วเก็บไว้
    await task  # รอให้ task ทำงานจนเสร็จ

asyncio.run(main())

