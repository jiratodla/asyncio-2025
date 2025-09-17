import time
import asyncio
import aiohttp

student_id = "6620301004"

async def fire_rocket(name: str, t0: float, session: aiohttp.ClientSession):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์

    async with session.get(url) as resp:
        data = await resp.json()
        time_to_target = data["time_to_target"]

    end_time = time.perf_counter() - t0

    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")

    names = ["Rocket-1", "Rocket-2", "Rocket-3"]

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fire_rocket(name, t0, session)) for name in names]

        results = await asyncio.gather(*tasks)

    # เรียงผลลัพธ์ตามเวลาที่ถึงเป้าหมายจริง (end_time)
    results.sort(key=lambda r: r["end_time"])

    print("Rockets fired:")
    for r in results:
        print(f'{r["name"]} | start_time: {r["start_time"]:.2f} sec | '
              f'time_to_target: {r["time_to_target"]:.2f} sec | end_time: {r["end_time"]:.2f} sec')

    t_total = max(r["end_time"] for r in results)
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")


if __name__ == "__main__":
    asyncio.run(main())
