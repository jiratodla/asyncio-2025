# example of starting many tasks and getting access to all tasks
import time
import asyncio

async def download_image(name, delay):
    print(f"{time.ctime()} {name} กำลังโหลด...")
    await asyncio.sleep(delay)
    print(f"{time.ctime()} {name} โหลดเสร็จแล้ว!")
    
async def main():
    print(f"{time.ctime()} main corotine started")
    delays = {2: 0,1:1,0:2}
    started_task = [asyncio.create_task(download_image(i , delays[i])) for i in range(3)]
    await asyncio.sleep(0.1)
    for task in started_task:
        await task

asyncio.run(main())
    



