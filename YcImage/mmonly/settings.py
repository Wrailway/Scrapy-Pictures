# -*- coding: utf-8 -*-
# Scrapy settings for mmonly project

BOT_NAME = 'mmonly'
SPIDER_MODULES = ['mmonly.spiders']
NEWSPIDER_MODULE = 'mmonly.spiders'
FEED_EXPORT_ENCODING = 'utf-8'

ROBOTSTXT_OBEY = False
#CONCURRENT_ITEMS = 200
# 默认是16，一次可以请求的最大次数
CONCURRENT_REQUESTS = 32
# 下载延迟
# DOWNLOAD_DELAY = 0.1
COOKIES_ENABLED = False
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

ITEM_PIPELINES = {'mmonly.pipelines.mmonlyPipeline': 100}

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
