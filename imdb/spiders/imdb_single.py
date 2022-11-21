import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = [
        'https://www.imdb.com/title/tt0068646',
    ]
    
    def parse(self, response, **kwargs):
        title = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/text()').get()
        release_date = response.xpath('/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/a/text()').get()
        cover_url = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/div[1]/img/@src').getall()
        genres = response.css('span.ipc-chip__text::text').getall()
        description = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]/text()').get()
        creator = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').get()
        country_of_origin = response.css('section[data-testid="Details"] li[data-testid="title-details-origin"] a::text').get()
        casts = response.css('section[data-testid="title-cast"] div[data-testid="shoveler"] div[data-testid="shoveler-items-container"] div[data-testid="title-cast-item"] a::text').getall()
        # casts = response.css('a.sc-bfec09a1-1::text').getall()
        language = response.css('section[data-testid="Details"] li[data-testid="title-details-languages"] a::text').get()
        run_time = response.css('section[data-testid="TechSpecs"] li[data-testid="title-techspec_runtime"] div::text').getall()
        rate = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()').getall()
        
        
        
        yield {
            'title':title,"language":language,'casts':casts,'release_date':release_date,
            'cover_url':cover_url,'genres':genres,'description':description,'creator':creator,
            'country_of_origin':country_of_origin,"run_time":run_time,'rate':rate
            }
        
        
