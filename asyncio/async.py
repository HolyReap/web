import asyncio
import datetime

import aiohttp
from more_itertools import chunked

from models import Base, Session, SwapiCharacters, engine

CHUNK_SIZE = 5


async def get_data(urls, key, client):
    data_list = []
    for url in urls:
        async with client.get(url) as response:
            json_data = await response.json()
            data_list.append(json_data.get(key))
    res = ', '.join(data_list)
    return res

async def counter(client):
    response = await client.get(f"https://swapi.py4e.com/api/people/")
    json_data = await response.json()
    await client.close()
    counter = json_data['count']
    return counter
 
async def get_people(client, people_id):
    response = await client.get(f"https://swapi.py4e.com/api/people/{people_id}")
    json_data = await response.json()
    
    if json_data.get('name'):
        films_c = get_data(json_data.get('films'),'title', client)
        homeworld_c = get_data(json_data.get('homeworld'),'name', client)
        species_c = get_data(json_data.get('species'),'name', client)
        starships_c = get_data(json_data.get('starships'),'name', client)
        vehicles_c = get_data(json_data.get('vehicles'),'name', client)
        
        fields = await asyncio.gather(films_c,homeworld_c,species_c,starships_c,vehicles_c)
        films, homeworld, species, starships, vehicles = fields
        json_data['id'] = people_id
        json_data['films'] = films
        json_data['homeworld'] = homeworld
        json_data['species'] = species
        json_data['starships'] = starships
        json_data['vehicles'] = vehicles
        del json_data['created']
        del json_data['edited']
        del json_data['url']
        return json_data
    else:
        return None

async def insert_data(p_data):
    async with Session() as session:
        session.add(SwapiCharacters(**p_data))
        await session.commit()
        
        
async def main():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)
    async with engine.begin() as con:
       await con.run_sync(Base.metadata.create_all)      
       
    async with aiohttp.ClientSession() as client:
        max_number = await counter(client)
        
    async with aiohttp.ClientSession() as client:
        for chunked_p in chunked(range(1,max_number), CHUNK_SIZE):
            person = await get_people(client, chunked_p)
            if person:
                asyncio.create_task(insert_data(person))
    
    all_tasks = asyncio.all_tasks()
    all_tasks = all_tasks - {asyncio.current_task()}
    await asyncio.gather(*all_tasks)
    
if __name__ == '__main__':
    start = datetime.datetime.now()
    asyncio.run(main())
    print(f"\n Time elapsed: {datetime.datetime.now() - start}")