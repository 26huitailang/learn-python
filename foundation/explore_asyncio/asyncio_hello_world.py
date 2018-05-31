import asyncio

@asyncio.coroutine
def hello():
    print("H")
    r = yield from asyncio.sleep(0.1)
    print("Again HW")

loop = asyncio.get_event_loop()
tasks = [hello() for x in range(10)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()