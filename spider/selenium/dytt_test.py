# coding: utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.dytt8.net/index.htm")
        self.assertIn("电影天堂", driver.title)
        # 下拉选项卡
        elem = driver.find_element_by_name("field")
        all_options = elem.find_elements_by_tag_name("option")
        for option in all_options:
            # print("Value is: %s, text is: %s" % (option.get_attribute("value"), option.get_text()))
            print("Value is: %s" % (option.get_attribute("value")))
            # 获取选项的文本信息
            print(option.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
