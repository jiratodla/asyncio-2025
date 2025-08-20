
import asyncio
import httpx

async def main():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Types:", [t["type"]["name"] for t in data["types"]])

asyncio.run(main())