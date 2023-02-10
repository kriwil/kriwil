AUTHOR = "aldi"
SITENAME = "kriwil.com"
SITEURL = "https://kriwil.com"

PATH = "content"

TIMEZONE = "Asia/Jakarta"

DEFAULT_LANG = "en"

PLUGINS = ["sitemap"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = True

# format
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
CATEGORY_URL = "{name}/"
CATEGORY_SAVE_AS = "{name}/index.html"
AUTHOR_URL = "author/{name}/"
AUTHOR_SAVE_AS = "author/{name}/index.html"
PAGE_URL = "page/{slug}/"
PAGE_SAVE_AS = "page/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_URL = "tags/"
TAGS_SAVE_URL = "tags/index.html"

SITEMAP = {
    "format": "xml",
    "changefreqs": {
        "articles": "daily",
        "pages": "daily",
        "indexes": "daily",
    },
    "exclude": ["tag/", "category/"],
}

CUSTOM_ARTICLE_URLS = {
    "links": {
        "URL": "{category}/{date:%Y%m%d}/{slug}/",
        "SAVE_AS": "{category}/{date:%Y%m%d}/{slug}/index.html",
    }
}


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    "format": "xml",
}
