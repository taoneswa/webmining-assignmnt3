import scrapy


class NewspapersclusSpider(scrapy.Spider):
    name = "newspapersclus"
    allowed_domains = ["standardspider.com"]
    start_urls = ["https://standardspider.com"]

    def parse(self, response):
        pass
