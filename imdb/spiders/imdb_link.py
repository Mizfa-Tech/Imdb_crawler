import scrapy
import re
from w3lib.html import remove_tags
from scrapy.loader import ItemLoader
from imdb.items import ImdbItem


class ImdbLinkSpider(scrapy.Spider):
    name = 'link'
    start_urls = [
        # 'https://www.imdb.com/search/title/?view=simple&count=250',
        'https://www.imdb.com/search/title/?view=simple'
    ]

    @staticmethod
    def _get_imdb_id(link):
        result = ''.join(re.findall("(tt\d+)", link))
        return result

    def parse(self, response, **kwargs):
        for item in response.css('span.lister-item-header'):
            title = item.css('a::text').get()
            link = self._get_imdb_id(item.css('a::attr(href)').get())
            yield {'title': title, 'link': link}

        next_page = response.css('div.desc a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
