# --coding:utf-8--
import os
import scrapy
import datetime
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from mmonly.items import mmonlyItem

class Myspider(CrawlSpider):
    """Spider that reads urls from redis queue (mmspider:start_urls)."""
    #allowed_domains = ['mmonly.cc']
    # start_urls = [
    #     'http://www.mmonly.cc/mmtp/',
    # ]
    ##scrapy-redis
    redis_key = "mmspider:strat_urls"
    
    name = 'mmspider'
    base = r'/home/yinchong/Downloads/mmtp/'

    rules = (
        Rule(LinkExtractor(allow=(''), restrict_xpaths=(u"//a[contains(text(),'下一页')]")), follow=True),
        Rule(LinkExtractor(allow=('http://www.mmonly.cc/(.*?).html'), restrict_xpaths=(u"//div[@class='ABox']")), callback="parse_item", follow=False),
    )
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = mmonlyItem()
        item['siteURL'] = response.url
        item['title'] = response.xpath('//h1/text()').extract_first()
        item['path'] = self.base + item['title']
        path = item['path']
        if not os.path.exists(path):
            os.makedirs(path)
        item['detailURL'] = response.xpath('//a[@class="down-btn"]/@href').extract_first()
        print(item['detailURL'] )
        num = response.xpath('//span[@class="nowpage"]/text()').extract_first()
        item['fileName'] = item['path'] + '/' + str(num) + '.jpg'

        print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), item['fileName'], u'解析成功！'
        yield item

        next_page = response.xpath(u"//a[contains(text(),'下一页')]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_item)
