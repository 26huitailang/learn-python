import asyncio
import aiohttp
import time

NUMBERS = range(1, 50 + 1)
URL = 'http://www.mzitu.com/135699/{}'
sema = asyncio.Semaphore(2)

async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.text()
        print(data)
    return data


async def print_result(a):
    with (await sema):
        r = await fetch_async(a)
        print('fetch({}) = {}'.format(a, r))

start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [print_result(num) for num in NUMBERS]
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
results = event_loop.run_until_complete(asyncio.wait(tasks))

print("Use asyncio+aiohttp cost: {}".format(time.time() - start))
