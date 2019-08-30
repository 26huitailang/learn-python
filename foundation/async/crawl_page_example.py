import asyncio


async def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split("_")[-1])
    await asyncio.sleep(sleep_time)
    print("OK {}".format(url))


async def main(urls):
    # 如果不创建task，直接await crawl_page方法的话相当于同步执行
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task
    # 另外一种写法
    # await asyncio.gather(*tasks)


asyncio.run(main(["url_1", "url_2", "url_3", "url_4"]))
