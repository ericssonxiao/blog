#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = "eric xiao"
SITENAME = "Eric Xiao's Blog"
#SITEURL = ""
SITETITLE = "Eric Xiao's Blog"
SITESUBTITLE = "Eric Xiao's Blog"
SITEDESCRIPTION = "Eric Xiao's Thoughts and Writings"
#SITELOGO = '/images/profile.png'
#FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#4682B4'
PYGMENTS_STYLE = 'default'
ROBOTS = 'index, follow'

PATH = 'content'
OUTPUT_PATH = 'blog/'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}
TIMEZONE = 'America/Montreal'

# Default theme language
I18N_TEMPLATE_LANG = 'en'

DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'blog/feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'blog/feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('about', '/pages/about.html'),
#          ('projects', '/pages/projects.html'),
#          ('slides', '/pages/slides.html'),)

# Social widget
SOCIAL = (('github', 'https://github.com/ericssonxiao'),
          ('linkedin', 'https://github.com/ericssonxiao'),
          ('facebook', 'https://github.com/ericssonxiao'),
          ('twitter', 'https://github.com/ericssonxiao'),
          ('rss', '/blog/feeds/all.atom.xml'),)

# Menu
DEFAULT_PAGINATION = 10
MAIN_MENU = True
HOME_HIDE_TAGS = True
USE_FOLDER_AS_CATEGORY = False
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


COPYRIGHT_YEAR = datetime.now().year

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = "/Users/ericxiao/Documents/pelican-themes/Flex"

# Sitemap
SITEMAP = {
    'format': 'xml',
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily',
    }
}

# STATIC
STATIC_PATHS = ['images', 'extra','projects','slides','CNAME']
CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

# Third page service , need to register
DISQUS_SITENAME = "ericssonxiao"
ADD_THIS_ID = 'ra-5e6fab73d0f4f611'

#GOOGLE_ANALYTICS = 'UA-1234-5678' need to register
# GOOGLE_ADSENSE = {
#     'ca_id': 'ca-pub-8640171181637141',
#     'page_level_ads': True,
#     'ads': {
#         'aside': '5604848266',
#         'main_menu': '',
#         'index_top': '',
#         'index_bottom': '2770021113',
#         'article_top': '',
#         'article_bottom': '4393383534',
#     }
# }
