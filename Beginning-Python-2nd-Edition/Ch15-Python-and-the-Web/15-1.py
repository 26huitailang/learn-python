#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple screen-scraping program

<h3><a name="google-mountain-view-ca-usa"><a class="reference"
href="http://www.google.com">Google</a> ...
"""
from urllib import urlopen
import re
p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://python.org/jobs').read()
for url, name in p.findall(text):
    print '%s (%s)' % (name, url)
