
import asyncio
import time

# ข้อมูลลูกค้าและสินค้า
customers = {
    "Alice": ["Apple", "Banana", "Milk"],
    "Bob": ["Bread", "Cheese"],
    "Charlie": ["Eggs", "Juice", "Butter"],
    "David": ["Tomato", "Lettuce", "Chicken", "Rice"],
    "Eva": ["Watermelon", "Yogurt"],
    "Frank": ["Coffee", "Sugar"],
    "Grace": ["Tea", "Biscuits", "Honey"],
    "Hannah": ["Cereal", "Milk", "Banana"],
    "Ian": ["Steak", "Potatoes"],
    "Jane": ["Fish", "Lemon", "Salt"]
}


# แคชเชียร์และเวลาประมวลผล (วินาทีต่อสินค้า)
cashiers = {
    "Cashier-1": 1,
    "Cashier-2": 2
    
}
async def customer_producer(queue, name, items):
    print(f"{time.ctime()} [{name}] finished shopping {items}")
    await queue.put((name, items))

async def cashier_consumer(queue, name, process_time):
    count_customers = 0
    while True:
        try:
            customer_name, items = await queue.get()
            count_customers += 1
            start_time = time.perf_counter()
            print(f"{time.ctime()} [{name}] processing {customer_name} with orders {items}")
            
            total_delay = process_time * len(items)
            await asyncio.sleep(total_delay)  # หน่วงเวลาแบบรวม
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"{time.ctime()} [{name}] finished {customer_name} {elapsed:.2f} seconds")
            queue.task_done()
        except asyncio.CancelledError:
            print(f"{time.ctime()} [{name}] closed have served {count_customers} customers")
            break


async def main():
    queue = asyncio.Queue(maxsize=5)

    # สร้าง producer task สำหรับลูกค้าแต่ละคน
    producers = [asyncio.create_task(customer_producer(queue, name, items)) for name, items in customers.items()]

    # สร้าง consumer task สำหรับแคชเชียร์แต่ละคน
    consumers = [asyncio.create_task(cashier_consumer(queue, name, time)) for name, time in cashiers.items()]

    # รอให้ producer ใส่งานทั้งหมดเข้า queue เสร็จ
    await asyncio.gather(*producers)

    # รอให้ queue ประมวลผลงานทั้งหมดเสร็จ (task_done ทุกชิ้น)
    await queue.join()

    # ยกเลิก consumer หลังจากงานทั้งหมดเสร็จ
    for consumer in consumers:
        consumer.cancel()

    # รอให้ consumer ทุกตัวปิดตัวอย่างปลอดภัย
    await asyncio.gather(*consumers, return_exceptions=True)

    print(f"{time.ctime()} [Main] Supermarket is closed!")

asyncio.run(main())

