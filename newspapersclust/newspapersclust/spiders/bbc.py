import scrapy


class BbcSpider(scrapy.Spider):
    name = "bbc"
    start_urls = [
        'https://www.bbc.com/business',
        'https://www.bbc.co.uk/arts',
        'https://www.bbc.com/sport',
        'https://www.bbc.com/news/politics'
    ]

    def parse(self, response):
        # Extract category from the updated structure
        category = response.css('div.brand-title h2 a.links::text').get()

        for article in response.css('div.card-body'):
            title = article.css('h3.mb-3 ::text').get()
            link = article.css('a.text-dark::attr(href)').get()
            content = article.css('div.mb-3.pt-2.top-article ::text').get()

            scraped_info = {
                'category': category,
                'title': title,
                'link': link,
                'content': content
            }
            yield scraped_info
