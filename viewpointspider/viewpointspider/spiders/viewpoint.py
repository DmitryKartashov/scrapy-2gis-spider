import scrapy


class ViewpointSpider(scrapy.Spider):
    name = 'viewpoint'
    allowed_domains = ['s.com']
    start_urls = ['http://s.com/']

    def parse(self, response):
        pass
