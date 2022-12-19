import scrapy
import re
from scrapy.loader import ItemLoader
from imdb.items import ImdbLinkItem


class ImdbLinkSpider(scrapy.Spider):
    name = 'link'
    start_urls = [
        'https://www.imdb.com/search/title/?view=simple&count=250',
        # 'https://www.imdb.com/search/title/?view=simple'
    ]

    @staticmethod
    def _get_imdb_id(link):
        result = ''.join(re.findall("(tt\d+)", link))
        return result

    def parse(self, response, **kwargs):
        for item in response.css('span.lister-item-header'):
            loader = ItemLoader(item=ImdbLinkItem(), selector=item)

            # _link = self._get_imdb_id(item.css('a::attr(href)').get())

            loader.add_css('title', 'a::text')
            # loader.add_value('link', _link)
            loader.add_css('link', 'a::attr(href)')

            yield loader.load_item()

        next_page = response.css('div.desc a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
