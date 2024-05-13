import scrapy


class BusinessSpider(scrapy.Spider):
    name = "business"
    allowed_domains = ["business.com"]
    start_urls = ["https://business.com"]

    def parse(self, response):
        pass
