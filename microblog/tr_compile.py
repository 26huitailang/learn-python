#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!flask/bin/python
import os
import sys
if sys.platform == 'wn32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'
os.system(pybabel + ' compile -d app/translations')
