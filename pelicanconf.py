AUTHOR = "aldi"
SITENAME = "kriwil"
SITEURL = "https://kriwil.com"

PATH = "content"

TIMEZONE = "Asia/Jakarta"

DEFAULT_LANG = "en"

PLUGINS = ["sitemap", "tailwindcss"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = False

DEFAULT_PAGINATION = 20

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

THEME = "theme/krwl2023"

STATIC_PATHS = [
    "static/favicon.ico",
]
EXTRA_PATH_METADATA = {
    "static/favicon.ico": {"path": "favicon.ico"},
}

TAILWIND = {
    "version": "3.2.7",
    "plugins": [
        "@tailwindcss/typography",
        # "@tailwindcss/forms",
        # "@tailwindcss/line-clamp",
        # "@tailwindcss/aspect-ratio",
    ],
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {},
        # "markdown.extensions.codehilite": {"css_class": "highlight"},
        # "markdown.extensions.extra": {},
        # "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
