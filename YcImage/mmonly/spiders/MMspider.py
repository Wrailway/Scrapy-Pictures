# --coding:utf-8--

import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mmonly.items import mmonlyItem


class Myspider(CrawlSpider):
    name = 'mmspider'
    base = r'/home/yinchong/Downloads/mmtp/'

    allowed_domains = ['mmonly.cc']
    start_urls = [
        'http://www.mmonly.cc/mmtp/',
    ]

    rules = (
        Rule(LinkExtractor(allow=(''), restrict_xpaths=(u"//a[contains(text(),'下一页')]")), follow=True),
        Rule(LinkExtractor(allow=('http://www.mmonly.cc/(.*?).html'), restrict_xpaths=(u"//div[@class='ABox']")), callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        item = mmonlyItem()
        item['siteURL'] = response.url
        item['title'] = response.xpath('//h1/text()').extract_first()
        item['fileName'] = self.base + item['title']
        fileName = item['fileName']
        if not os.path.exists(fileName):
            os.makedirs(fileName)
        item['detailURL'] = response.xpath('//a[@class="down-btn"]/@href').extract_first()
        print(item['detailURL'] )
        num = response.xpath('//span[@class="nowpage"]/text()').extract_first()
        item['path'] = item['fileName'] + '/' + str(num) + '.jpg'

        yield item

        next_page = response.xpath(u"//a[contains(text(),'下一页')]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_item)

