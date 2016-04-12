#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!flask/bin/python
import os
import sys
if sys.platform == 'wn32':
    pybabel = 'pybabel'
else:
    pybabel = 'pybabel'
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot app')
os.system(pybabel + ' update -i messages.pot -d app/translations')
os.unlink('messages.pot')
