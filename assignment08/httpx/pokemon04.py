import asyncio
import httpx
import time

pokemon_names = ['pikachu','bulbasaur','charmander','squirtle','eevee','snorlax','gengar','mewtwo','psyduck','jigglypuff']
async def fetch_pokemon_data(client, name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(f"{data['name'].title()} -> ID: {data['id']}, Types: {[t['type']['name'] for t in data['types']]}")

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch_pokemon_data(client, name) for name in pokemon_names]
        await asyncio.gather(*tasks)

asyncio.run(main())