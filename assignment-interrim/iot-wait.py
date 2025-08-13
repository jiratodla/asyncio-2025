import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay
    return " Temp: 30°C"  # Simulated temperature value
async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay
    return " Humidity: 60%"  # Simulated humidity value
async def get_weather_api():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay
    return " Weather: Sunny"  # Simulated weather condition

async def main():
    start_time = time.perf_counter()
    tasks = [
        get_temperature(),
        get_humidity(),
        get_weather_api()
    ]

    # แสดงผลทันทีที่ task เสร็จ
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"{time.ctime()} --> {result}")

    elapsed = time.perf_counter() - start_time
    print(f"Took: {elapsed:.2f} seconds")

asyncio.run(main())