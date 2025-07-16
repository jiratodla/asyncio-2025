import asyncio
import httpx
import time

pokemon_names = ['pikachu','bulbasaur','charmander','squirtle','eevee','snorlax','gengar','mewtwo','psyduck','jigglypuff']
async def fetch_pokemon_data(client, name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = await client.get(url)
    data = response.json()
    return {
        'name': data['name'].title(),
        'id': data['id'],
        'base_experience': data['base_experience']
    }
async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch_pokemon_data(client, name) for name in pokemon_names]
        result = await asyncio.gather(*tasks)
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                if result[i]['base_experience'] < result[j]['base_experience']:
                    result[i], result[j] = result[j], result[i]
    for p in result:
            print(f"{p['name']} -> ID: {p['id']}, Base XP: {p['base_experience']}")

asyncio.run(main())