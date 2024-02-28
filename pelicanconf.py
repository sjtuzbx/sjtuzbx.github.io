#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'zbx'
SITENAME = "Beta's Note"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh-cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-themes/Flex'
SITETITLE = "Beta's Note"
SITESUBTITLE = "一个想找工作的Coder/c++/Python/ai"
# SITESUBTITLE2 = "work hard, keep steady"
SITELOGO = "https://avatars.githubusercontent.com/u/36227079?s=400&u=36f9635e7f0d57d279ea72a20ac16b8eac71521e&v=4"

# Blogroll
# LINKS = (('Github', 'https://github.com/sjtuzbx'),
#         ('Blogger', 'https://stupidbookfish.blogspot.com/'))

LINKS = (
    ("文章列表", "/archives.html"),
)

SOCIAL = (
    ("github", "https://github.com/sjtuzbx"),
)

MENUITEMS = (
    ("文章列表", "/archives.html"),
)
DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# math
PLUGIN_PATHS=['pelican-plugins']
PLUGINS = ["render_math"]

## load cache
LOAD_CONTENT_CACHE = False

## typogrify
TYPOGRIFY = True

# font
USE_GOOGLE_FONTS = True

# other settings
MAIN_MENU = True

SUMMARY_MAX_LENGTH = 30

STATIC_PATHS = [
    "images",
    "extra/custom.css",
    "extra/favicon.ico",
]

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/favicon.ico": {"path": "static/favicon.ico"},
}

CUSTOM_CSS = 'static/custom.css'
FAVICON = 'static/favicon.ico'

