import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup


def sync_main():
    """cost 1min"""
    url = "https://movie.douban.com/cinema/later/chengdu/"
    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, "lxml")

    all_movies = init_soup.find("div", id="showing-soon")
    # print(all_movies)
    for movie in all_movies.find_all("div", class_="item"):
        all_a_tag = movie.find_all("a")
        all_li_tag = movie.find_all("li")

        name = all_a_tag[1].text
        date = all_li_tag[0].text
        detail = all_a_tag[0].attrs["href"]

        init_detail_page = requests.get(detail).content
        init_detail_soup = BeautifulSoup(init_detail_page, "lxml")
        poster = init_detail_soup.find("div", id="mainpic").a.img.attrs["src"]

        print(f"{name} {date} {poster}")


async def get_url_content(url):
    async with aiohttp.ClientSession() as session:
        html = await session.get(url)
        return await html.text()


async def async_main():
    url = "https://movie.douban.com/cinema/later/chengdu/"
    init_page = await get_url_content(url)
    init_soup = BeautifulSoup(init_page, "lxml")

    all_movies = init_soup.find("div", id="showing-soon")

    names, dates, url_to_fetch = [], [], []
    for movie in all_movies.find_all("div", class_="item"):
        all_a_tag = movie.find_all("a")
        all_li_tag = movie.find_all("li")

        names.append(all_a_tag[1].text)
        dates.append(all_li_tag[0].text)
        url_to_fetch.append(all_a_tag[0].attrs["href"])

    tasks = [get_url_content(x) for x in url_to_fetch]
    pages = await asyncio.gather(*tasks)  # gather 可以不用在前面create_task，如果直接await task的话，要提前创建

    for name, date, page in zip(names, dates, pages):
        init_detail_soup = BeautifulSoup(page, "lxml")
        poster = init_detail_soup.find("div", id="mainpic").a.img.attrs["src"]

        print(f"{name} {date} {poster}")


if __name__ == "__main__":
    # sync_main()  # 1min
    asyncio.run(async_main())  # 7s
