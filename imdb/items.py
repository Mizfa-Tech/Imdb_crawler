# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders import processors


def run_time(value: list[str]):
    return ''.join(value)


def validate_data(value):
    if value:
        return value
    return 'NULL'


class ImdbItem(scrapy.Item):
    imdb_id = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    title = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    release_date = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    cover_url = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    genres = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    description = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    director = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    writers = scrapy.Field(input_processor=processors.Compose(validate_data), output_processor=processors.Identity())
    country_of_origin = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    language = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    run_time = scrapy.Field(input_processor=processors.Compose(run_time), output_processor=processors.TakeFirst())
    rate = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    rete_population = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    casts = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    stars = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    film_location = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    budget = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    color = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    sound_mix = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    aspect_ratio = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    production_companies = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    certificate = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.Identity())
    oscars = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
    awards = scrapy.Field(input_processor=processors.Compose(validate_data),output_processor=processors.TakeFirst())
