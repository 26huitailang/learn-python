#!/usr/bin/python
# coding: utf-8

import unittest
from unittest import mock

from project import get_suit_from_mzitu_by_suit_url


class TestOneSuit(unittest.TestCase):

    html = "aaaaaaaaaaaaaa<span>5</span><h1></h1>aaaaaa\n<span>10</span>"

    def test_success_get_max_page_num(self):
        resp = get_suit_from_mzitu_by_suit_url.get_max_page_num(self.html)
        self.assertEqual(resp, 10)
