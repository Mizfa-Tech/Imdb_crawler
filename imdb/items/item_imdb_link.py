import scrapy
from itemloaders import processors
from imdb.items.processors import get_imdb_id, validate_data, run_time


# ------------------------------------------------ Item ________________________________________________________________

class ImdbLinkItem(scrapy.Item):
    title = scrapy.Field(input_processor=processors.Compose(validate_data), output_processor=processors.TakeFirst())
    imdb_id = scrapy.Field(input_processor=processors.MapCompose(validate_data, get_imdb_id),
                           output_processor=processors.TakeFirst())
