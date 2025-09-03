import asyncio
import httpx

servers = [
    "http://172.20.49.87:8000",
    "http://172.20.49.70:8000",
    "http://172.20.50.15:8000"
]

endpoints = ["/students", "/analytics/group", "/analytics/enrolled_year"]

async def fetch_endpoint(client, server, endpoint):
    url = f"{server}{endpoint}"
    try:
        resp = await client.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

async def fetch_all_for_server(client, server):
    results = []

    # ดึง /students
    students = await fetch_endpoint(client, server, "/students")
    if isinstance(students, str) and students.startswith("Error:"):
        results.append({"server": server, "student_count": students})
    else:
        results.append({"server": server, "student_count": len(students)})


    # ดึง /analytics/group
    group = await fetch_endpoint(client, server, "/analytics/group")
    if isinstance(group, dict) and "error" in group:
        results.append({"server": server, "group_analytics": f"Error: {group['error']}"})
    else:
        results.append({"server": server, "group_analytics": group})

    # ดึง /analytics/year
    year = await fetch_endpoint(client, server, "/analytics/enrolled_year")
    if isinstance(year, dict) and "error" in year:
        results.append({"server": server, "year_analytics": f"Error: {year['error']}"})
    else:
        results.append({"server": server, "year_analytics": year})

    return results

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch_all_for_server(client, server) for server in servers]
        all_results = await asyncio.gather(*tasks)

    # รวมผลลัพธ์จากทุก server และ flatten list ออกมา
    flat_results = [item for sublist in all_results for item in sublist]

    # แสดงผลลัพธ์ตามรูปแบบที่ต้องการ
    for res in flat_results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())