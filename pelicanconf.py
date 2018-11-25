#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vincent La'
SITENAME = 'Vincent La'
SITEURL = ''

STATIC_PATHS = ['assets', 'images']

PATH = 'content'
PAGE_PATHS = ['pages']
PATH_METADATA = r'(pages/)?(?P<pathto>.*)[\.]'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['autopages', ]

# Makes plugins that work with content (e.g. autopages) work
LOAD_CONTENT_CACHE = False

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'
USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Custom Theme
THEME = 'themes/vince-theme'
MAIN_MENU = (
             ('About', '/about'),
             ('Blog', '/blog'),
             ('Projects', '/projects'),
             ('Resume', '/resume')
            )

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URLs
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '{pathto}'
ARTICLE_SAVE_AS = '{pathto}/index.html'

PAGE_URL = '{pathto}/'
PAGE_SAVE_AS = '{pathto}/index.html'

# Order articles by filename
ARTICLE_ORDER_BY = 'source_path'