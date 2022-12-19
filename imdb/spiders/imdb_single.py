import re
import scrapy
from scrapy.loader import ItemLoader
from imdb.items import ImdbItem


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = [
        'https://www.imdb.com/title/tt1759761/',
    ]

    def parse(self, response, **kwargs):
        loader = ItemLoader(item=ImdbItem(), response=response)

        loader.add_value('imdb_id', response.url)

        loader.add_css('title', 'h1[data-testid="hero-title-block__title"]::text')

        loader.add_css('release_date', 'li[data-testid="title-details-releasedate"] div a::text')

        loader.add_css('cover_url', 'div[data-testid="hero-media__poster"] div.ipc-media img::attr(src)')

        loader.add_css('genres', 'div[data-testid="genres"] div.ipc-chip-list__scroller a span::text')

        loader.add_css('description', 'span[data-testid="plot-xl"]::text')

        loader.add_xpath('director',
                         '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[1]/div/ul/li/a/text()')

        loader.add_xpath('writers',
                         '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[2]/div/ul/li/a/text()')

        loader.add_css('country_of_origin',
                       'section[data-testid="Details"] li[data-testid="title-details-origin"] a::text')

        loader.add_css('language', 'section[data-testid="Details"] li[data-testid="title-details-languages"] a::text')

        loader.add_css('run_time',
                       'li[data-testid="title-techspec_runtime"] div::text')

        loader.add_xpath('rate',
                         '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()')

        loader.add_xpath('rete_population',
                         '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[3]/text()')

        loader.add_css('film_location', 'li[data-testid="title-details-companies"] div ul li a::text')

        loader.add_css('budget', 'li[data-testid="title-boxoffice-budget"] div ul li label::text')

        loader.add_css('color', 'li[data-testid="title-techspec_color"] a::text')

        loader.add_css('sound_mix', 'li[data-testid="title-techspec_soundmix"] li a::text')

        loader.add_css('aspect_ratio', 'li[data-testid="title-techspec_aspectratio"] li label::text')

        loader.add_css('production_companies', 'li[data-testid="title-details-companies"] div a::text')

        loader.add_css('certificate', 'li[data-testid="storyline-certificate"] div label::text')

        loader.add_css('oscars', 'li[data-testid="award_information"] a::text')

        loader.add_css('awards', 'li[data-testid="award_information"] div label::text')

        casts = response.css(
            'section[data-testid="title-cast"] div[data-testid="shoveler"] div[data-testid="shoveler-items-container"] div[data-testid="title-cast-item"] a::text').getall()
        casts_character = response.css('a[data-testid="cast-item-characters-link"] span::text').getall()

        final_casts = dict(zip(casts, casts_character))
        loader.add_value('casts', final_casts)

        loader.add_xpath('stars',
                         '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li/a/text()')

        yield loader.load_item()
