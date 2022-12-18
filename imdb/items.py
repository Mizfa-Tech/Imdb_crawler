# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders import processors


def run_time(value: list[str]):
    hours, minutes = value[0], value[4]
    return f"{hours} hours {minutes} minutes"


def get_certificate(value: list[str]):
    certificate = value[1]
    return certificate


class ImdbItem(scrapy.Item):
    imdb_id = scrapy.Field(output_processor=processors.TakeFirst())
    title = scrapy.Field(output_processor=processors.TakeFirst())
    release_date = scrapy.Field(output_processor=processors.TakeFirst())
    cover_url = scrapy.Field(output_processor=processors.TakeFirst())
    genres = scrapy.Field(output_processor=processors.Identity())
    description = scrapy.Field(output_processor=processors.TakeFirst())
    director = scrapy.Field(output_processor=processors.Identity())
    writers = scrapy.Field(output_processor=processors.Identity())
    country_of_origin = scrapy.Field(output_processor=processors.TakeFirst())
    language = scrapy.Field(output_processor=processors.Identity())
    run_time = scrapy.Field(input_processor=processors.Compose(run_time), output_processor=processors.TakeFirst())
    rate = scrapy.Field(output_processor=processors.TakeFirst())
    rete_population = scrapy.Field(output_processor=processors.TakeFirst())
    casts = scrapy.Field(output_processor=processors.TakeFirst())
    stars = scrapy.Field(output_processor=processors.Identity())
    film_location = scrapy.Field(output_processor=processors.Identity())
    budget = scrapy.Field(output_processor=processors.TakeFirst())
    color = scrapy.Field(output_processor=processors.TakeFirst())
    sound_mix = scrapy.Field(output_processor=processors.Identity())
    aspect_ratio = scrapy.Field(output_processor=processors.TakeFirst())
    production_companies = scrapy.Field(output_processor=processors.Identity())
    certificate = scrapy.Field(output_processor=processors.Identity())
    oscars = scrapy.Field(output_processor=processors.TakeFirst())
    awards = scrapy.Field(output_processor=processors.TakeFirst())
