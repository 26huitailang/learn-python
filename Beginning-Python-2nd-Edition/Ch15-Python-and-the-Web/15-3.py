#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
<h2 class="listing-company">
<span class="listing-company-name">
<span class="listing-new">New</span> <a href="/jobs/2126/"> C++/Python Software Engineer</a><br/>
                    Core Security
                </span>
<span class="listing-location"><a href="/jobs/location/palermo-buenos-aires-argentina/" title="More jobs in Palermo, Buenos Aires, Argentina">
Palermo, Buenos Aires, Argentina</a></span>
</h2>
"""
from urllib import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://www.python.org/jobs').read()
soup = BeautifulSoup(text, "lxml")
# print soup

jobs = set()
for header in soup('h2'):
    links = header('a')
    if not links:
        continue
    link = links[0]
    jobs.add('%s (%s)' % (link.string, link['href']))

print '\n'.join(sorted(jobs, key=lambda s: s.lower()))
