# example of using an asyncio queue
from random import random
import asyncio

async def producer(queue):
    for i in range(10):
        value = random() * 10
        await asyncio.sleep(random())
        print(f"Produced {value}")
        await queue.put(value)
    await queue.put(None) 
    print("Producer : Done")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        
        print(f'\t>Consumer got {item}')
    print("Consumer : Done")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))
asyncio.run(main())
