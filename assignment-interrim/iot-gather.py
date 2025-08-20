import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay
    return f"{time.ctime()} Temp: 30°C"  # Simulated temperature value
async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay
    return f"{time.ctime()} Humidity: 60%"  # Simulated humidity value
async def get_weather():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate network delay
    return f"{time.ctime()} Weather: Sunny"  # Simulated weather condition
async def main():
    start = time.time()
    temp = await get_temperature()
    humidity = await get_humidity()
    weather = await get_weather()
    end = time.time()
    print(f"All tasks completed in {end - start:.2f} seconds")
    print(temp)
    print(humidity)
    print(weather)

asyncio.run(main())
