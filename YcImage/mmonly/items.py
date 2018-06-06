# -*- coding: utf-8 -*-
import scrapy

class mmonlyItem(scrapy.Item):
    siteURL = scrapy.Field()
    pageURL = scrapy.Field()
    detailURL = scrapy.Field()
    title = scrapy.Field()
    fileName = scrapy.Field()
    path = scrapy.Field()
