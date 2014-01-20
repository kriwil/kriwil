#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'aldi'
SITENAME = u'kriwil.com'
SITEURL = ''

TIMEZONE = 'Asia/Jakarta'

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

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

TWITTER_USERNAME = 'kriwil'
DISQUS_SITENAME = 'kriwil'
GOOGLE_ANALYTICS = 'UA-2022719-1'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
