import asyncio
import random


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print("{} get a val: {}".format(id, val))
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print(f"{id} put a val {val}")
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()

    consumer_1 = asyncio.create_task(consumer(queue, "consumer_1"))
    consumer_2 = asyncio.create_task(consumer(queue, "consumer_2"))

    producer_1 = asyncio.create_task(producer(queue, "producer_1"))
    producer_2 = asyncio.create_task(producer(queue, "producer_2"))

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
