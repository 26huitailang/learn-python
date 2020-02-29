from abc import ABCMeta, abstractmethod, abstractproperty
from bs4 import BeautifulSoup
import requests


class BasePage(metaclass=ABCMeta):
    @abstractproperty
    def suites(self):
        pass

    @abstractproperty
    def next_page(self):
        pass

    @abstractmethod
    def download(self):
        pass


class BaseSuite(metaclass=ABCMeta):
    @abstractproperty
    def images(self):
        pass

    @abstractproperty
    def next_page(self):
        pass

    @abstractmethod
    def download(self):
        pass


class BaseImage(metaclass=ABCMeta):
    @abstractmethod
    def download(self):
        pass


class MTRImage(BaseImage):
    def __init__(self, url, suite_name):
        self._url = url
        self._suite_name = suite_name

    def download(self):
        print("download {} {}".format(self._suite_name, self._url))


class MTRSuite(BaseSuite):
    ImageCls = MTRImage

    def __init__(self, name, url):
        self._name = name
        self._url = url
        self._images = []
        self.content_cache = {}
        self.cur_div_pages = None
        self.is_last_page = False
        self._parse_images()

    @property
    def images(self):
        return self._images

    @property
    def next_page(self):
        print(self._url)
        if self.is_last_page:
            return
        next_page = self.cur_div_pages.find_all("a")[-1]
        cur_page = self.cur_div_pages.find_all("span")[0]
        if cur_page.text == next_page.attrs["href"].split("/")[-1].split(".")[0]:
            self.is_last_page = True
        return next_page.attrs["href"]

    def download(self):
        for image in self._images:
            image.download()

    def _cache_content(self, url, content):
        if url not in self.content_cache:
            self.content_cache[url] = content

    def _get_content(self, url):
        if url in self.content_cache:
            return self.content_cache[url]
        html = requests.get(url)
        self._cache_content(url, html.content)
        return html.content

    def _parse_images(self):
        while True:
            if not self._url:
                break
            html_content = self._get_content(self._url)
            init_page = BeautifulSoup(html_content, "lxml")
            self.cur_div_pages = init_page.find("div", id="pages")
            init_div_content = init_page.find("div", class_="content")

            for img_tag in init_div_content.find_all("img"):
                img = self.ImageCls(img_tag.attrs["src"], self._name)
                self._images.append(img)

            if self.next_page:
                self._url = self.next_page


class MTRThemePage(BasePage):
    SuiteCls = MTRSuite

    def __init__(self, url):
        self._url = url
        self._pages = []
        self._suites = []
        self._name = None
        self._parse_suites()

    @property
    def suites(self):
        return self._suites

    @property
    def next_page(self):
        return

    def download(self):
        for suite in self._suites:
            suite.download()

    def _parse_suites(self):
        raise NotImplementedError()


class MTRSearchPage(BasePage):
    SuiteCls = MTRSuite

    def __init__(self, url):
        self._url = url
        self._pages = []
        self._suites = []
        self._name = None
        self._parse_suites()

    @property
    def suites(self):
        return self._suites

    @property
    def next_page(self):
        return

    def download(self):
        for suite in self._suites:
            suite.download()

    def _parse_suites(self):
        html = requests.get(self._url)
        init_page = BeautifulSoup(html.content, "lxml")
        ul_img_tag = init_page.find("ul", class_="img")

        for li_tag in ul_img_tag.find_all("li"):
            suite_name = li_tag.p.text
            suite_url = li_tag.a.attrs["href"]
            suite = self.SuiteCls(suite_name, suite_url)
            self._suites.append(suite)


class Crawl(object):
    def __init__(self, content):
        self.content = content
        self.downloader = None
        if self.is_mtr_theme_page:
            self.downloader = MTRThemePage(self.content)
        elif self.is_mtr_search_page:
            self.downloader = MTRSearchPage(self.content)
        else:
            raise ValueError("unknown type {}".format(content))
        return

    @property
    def is_mtr_theme_page(self):
        if "www.meituri.com/x/" in self.content:
            return True
        return False

    @property
    def is_mtr_search_page(self):
        if "www.meituri.com/search/" in self.content:
            return True
        return False


if __name__ == "__main__":
    content_search = "https://www.meituri.com/search/婉萍"
    content_theme = "https://www.meituri.com/x/82/"
    crawl = Crawl(content_search)
    crawl.downloader.download()
