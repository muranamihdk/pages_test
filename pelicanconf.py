#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pages'
SITENAME = 'Pages Test Site'
SITEURL = 'https://muranamihdk.github.io/pages_test'
#SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output/'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y年%m月%d日(%a)'
LOCALE = 'ja_JP'

#THEME = "simple"
#THEME = "notmyidea"
THEME = "themes/mycustomtheme"

DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = ['plugins']
#PLUGINS = ['page_hierarchy', 'my_generator']
PLUGINS = ['page_hierarchy']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'nl2br', 'sane_lists', 'denden_extension']

SLUGIFY_SOURCE = 'basename'

PAGE_PATHS = ['']
#PAGE_EXCLUDES = ['my_page']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
#PAGE_LANG_URL = '{slug}-{lang}.html'
#PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

#MY_PAGE_PATHS = ['my_page']
#MY_PAGE_EXCLUDES = ['']
#MY_PAGE_ORDER_BY = 'basename'

ARTICLE_PATHS = ['articles']
#ARTICLE_URL = 'article/{slug}.html'
#ARTICLE_SAVE_AS = 'article/{slug}.html'

#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']
#DIRECT_TEMPLATES = ['categories', 'tags']
DIRECT_TEMPLATES = []
#CATEGORIES_SAVE_AS = 'article/categories.html'
#TAGS_SAVE_AS = 'article/tags.html'

#CATEGORY_URL = 'article/category/{slug}.html'
#CATEGORY_SAVE_AS = 'article/category/{slug}.html'
#TAG_URL = 'article/tag/{slug}.html'
#TAG_SAVE_AS = 'article/tag/{slug}.html'
#AUTHOR_URL = 'article/tag/{slug}.html'
#AUTHOR_SAVE_AS = 'article/tag/{slug}.html'

#CATEGORY_SAVE_AS = ''
#TAG_SAVE_AS = ''
#AUTHOR_SAVE_AS = ''

USE_FOLDER_AS_CATEGORY = False
#DEFAULT_CATEGORY = 'misc'

#TEMPLATE_PAGES = {'context.html': 'context.html'}

IGNORE_FILES = ['.DS_Store', '__pycache__']

