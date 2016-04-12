# -*- coding: utf-8 -*-
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True # UserWarning

# mail server settings
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
# MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = '50590960'
MAIL_PASSWORD = 'gsuzrbmkxhvybiac' # qq: gsuzrbmkxhvybiac csj123456

#administrator list
ADMINS = ['50590960@qq.com', 'chensijian199182@163.com', '26huitailang@gmail.com']

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'zn-Hans-CN': 'Chinese'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = '26huitailang' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'yQF6yr+T7Pf1ew57r+6xsZLrDkan70vusGlGvFn2bp8=' # enter your MS translator app secret here