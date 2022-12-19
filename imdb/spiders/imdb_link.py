import scrapy
from imdb.items import ImdbLinkItem
from scrapy.loader import ItemLoader


class ImdbLinkSpider(scrapy.Spider):
    name = 'link'
    start_urls = [
        'https://www.imdb.com/search/title/?view=simple&count=250',
        # 'https://www.imdb.com/search/title/?view=simple'
    ]

    def parse(self, response, **kwargs):
        for item in response.css('span.lister-item-header'):
            loader = ItemLoader(item=ImdbLinkItem(), selector=item)
            loader.add_css('title', 'a::text')
            loader.add_css('link', 'a::attr(href)')

            yield loader.load_item()

        next_page = response.css('div.desc a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
