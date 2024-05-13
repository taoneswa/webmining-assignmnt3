import scrapy


class ArtsculturecelebSpider(scrapy.Spider):
    name = "artscultureceleb"
    allowed_domains = ["artscultureceleb.com"]
    start_urls = ["https://artscultureceleb.com"]

    def parse(self, response):
        pass
