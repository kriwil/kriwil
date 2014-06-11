#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'aldi'
SITENAME = u'kriwil.com'
SITEURL = ''

TIMEZONE = 'Asia/Jakarta'

THEME = 'pelican-cait'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# format
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
CATEGORY_URL = 'category/{name}/'
CATEGORY_SAVE_AS = 'category/{name}/index.html'
AUTHOR_URL = 'author/{name}/'
AUTHOR_SAVE_AS = 'author/{name}/index.html'

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 5

DISQUS_SITENAME = 'kriwil'
TWITTER_USERNAME = 'kriwil'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
