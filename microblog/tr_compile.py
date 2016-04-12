#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!flask/bin/python
import os
import sys
if sys.platform == 'wn32':
    pybabel = 'pybabel'
else:
    pybabel = 'pybabel'
os.system(pybabel + ' compile -d app/translations')
