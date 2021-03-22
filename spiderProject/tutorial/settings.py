# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False



# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 降低下载延迟
DOWNLOAD_DELAY = 0

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# scrapy框架是基于多线程Twisted，当然scrapy也是通过多线程进行数据请求的，并且支持多核CPU的并发，我们就可以通过设置并发请求数来提高爬取速度。
CONCURRENT_REQUESTS = 100
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
# 禁止使用Cookies
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 管道激活
ITEM_PIPELINES = {
    'tutorial.pipelines.TutorialPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# 自动限速拓展AutoThrottle,设置和多线程一致提高速度
AUTOTHROTTLE_TARGET_CONCURRENCY = 100
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 默认显示的中文是阅读性较差的Unicode字符
from scrapy.exporters import JsonLinesItemExporter


# 需要定义子类显示出原来的字符集（将父类的ensure_ascii属性设置为False即可）
class CustomJsonLinesItemExporter(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super(CustomJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)

    # 启用新定义的Exporter类\
    FEED_EXPORTERS = {
        'json': 'stockstar.settings.CustomJsonLinesItemExporter',
    }
    ...
    # Configure a delay for requests for the same website (default: 0)
    # See http:IIscrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
    # See also autothrottle settings and docs DOWNLOAD DELAY = 0.25
