# coding: utf-8
"""
https://zhuanlan.zhihu.com/p/27258289
"""
import time
import asyncio
import random


class Potato(object):
    @classmethod
    def make(cls, num, *args, **kwargs):
        items = []
        for i in range(num):
            items.append(cls.__new__(cls, *args, **kwargs))
        return items


class Juice(object):
    @classmethod
    def make(cls, num, *args, **kwargs):
        items = []
        for i in range(num):
            items.append(cls.__new__(cls, *args, **kwargs))
        return items


# 同步实现，会一直等待
def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            time.sleep(0.1)
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break


def buy_potatos():
    bucket = []
    for p in take_potatos(50):
        bucket.append(p)
        print(bucket)


# 异步实现，当货架上没有土豆的时候，问更多的货，补货的时候可以买其他东西
async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))


async def take_potatos_async(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break


async def buy_potatos_async():
    bucket = []
    # 异步迭代
    async for p in take_potatos_async(50):
        bucket.append(p)
        print(f'Got potato {id(p)}')


async def take_juice_async():
    while True:
        if len(all_juices) == 0:
            break
        juice = all_juices.pop()
        yield juice


async def buy_all_juice_async():
    bucket = []
    async for p in take_juice_async():
        bucket.append(p)
        await asyncio.sleep(random.random())
        print(f'Got juice {id(p)}')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.wait(
            [buy_potatos_async(), buy_all_juice_async()]
        )
    )
    loop.close()


if __name__ == '__main__':
    all_potatos = Potato.make(5)
    all_juices = Juice.make(20)
    main()
