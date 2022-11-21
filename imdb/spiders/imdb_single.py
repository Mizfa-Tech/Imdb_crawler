import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = [
        'https://www.imdb.com/title/tt0111161/',
    ]
    
    def parse(self, response, **kwargs):
        title = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/text()').get()
        release_date = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[12]/div[2]/ul/li[1]/div/ul/li/a/text()').get()
        cover_url = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/div[1]/img/@src').getall()
        genres = response.css('span.ipc-chip__text::text').getall()
        description = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]/text()').get()
        creator = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').get()
        country_of_origin = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[12]/div[2]/ul/li[2]/div/ul/li/a/text()').get()
        casts = response.css('a.sc-bfec09a1-1::text').getall()
        language = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[12]/div[2]/ul/li[4]/div/ul/li/a/text()').get()
        
        yield {
            'title':title,"language":language,'casts':casts,'release_date':release_date,
            'cover_url':cover_url,'genres':genres,'description':description,'creator':creator,
            'country_of_origin':country_of_origin
            }
        
        
