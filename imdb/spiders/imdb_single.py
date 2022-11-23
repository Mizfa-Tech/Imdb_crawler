import scrapy
import re
from scrapy.loader import ItemLoader
from imdb.items import ImdbItem


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = [
        'https://www.imdb.com/title/tt0068646',
        'https://www.imdb.com/title/tt0468569',
        'https://www.imdb.com/title/tt9288822',
        'https://www.imdb.com/title/tt0292506',
        'https://www.imdb.com/title/tt0159273',
        'https://www.imdb.com/title/tt0314353',
    ]
    
    def parse(self, response, **kwargs):
        loader = ItemLoader(item=ImdbItem(),response=response)
        
        
        imdb_id = re.findall("tt\d{7}",response.url)[0]
        loader.add_value('imdb_id',imdb_id)
    
    
        # title = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/text()').get()
        # title = response.css('h1[data-testid="hero-title-block__title"]::text').get()
        loader.add_css('title','h1[data-testid="hero-title-block__title"]::text')
        
        
        # # release_date = response.xpath('/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/a/text()').get()
        # # release_date = response.css('li[data-testid="title-details-releasedate"] div a::text').get()
        loader.add_css('release_date','li[data-testid="title-details-releasedate"] div a::text')
        
        
        # # cover_url = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/div[1]/img/@src').getall()
        # # cover_url = response.css('div[data-testid="hero-media__poster"] div.ipc-media img::attr(src)').get()
        loader.add_css('cover_url','div[data-testid="hero-media__poster"] div.ipc-media img::attr(src)')

        
        # # genres = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/span/text()').getall()
        # # genres = response.css('div[data-testid="genres"] div.ipc-chip-list__scroller a span::text').getall()
        loader.add_css('genres','div[data-testid="genres"] div.ipc-chip-list__scroller a span::text')
        
        
        # # description = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]/text()').get()
        # # description = response.css('span[data-testid="plot-xl"]::text').get()
        loader.add_css('description','span[data-testid="plot-xl"]::text')
        
        # # director = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').get()
        # # director = response.css('li[data-testid="title-pc-principal-credit"] div a::text').get()
        loader.add_xpath('director','//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[1]/div/ul/li/a/text()')
        
        loader.add_xpath('writers','//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[2]/div/ul/li/a/text()')
      
      
        # # country_of_origin = response.css('section[data-testid="Details"] li[data-testid="title-details-origin"] a::text').get()
        loader.add_css('country_of_origin','section[data-testid="Details"] li[data-testid="title-details-origin"] a::text')
        
        
        # # language = response.css('section[data-testid="Details"] li[data-testid="title-details-languages"] a::text').get()
        loader.add_css('language','section[data-testid="Details"] li[data-testid="title-details-languages"] a::text')
        
        
        # # run_time = response.css('section[data-testid="TechSpecs"] li[data-testid="title-techspec_runtime"] div::text').getall()
        loader.add_css('run_time','section[data-testid="TechSpecs"] li[data-testid="title-techspec_runtime"] div::text')
        
        # # rate = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()').get()
        loader.add_xpath('rate','//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()')
        
        # # rete_population = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[3]/text()').get()
        loader.add_xpath('rete_population','//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[3]/text()')
        
        casts = response.css('section[data-testid="title-cast"] div[data-testid="shoveler"] div[data-testid="shoveler-items-container"] div[data-testid="title-cast-item"] a::text').getall()
        casts_charcter = response.css('a[data-testid="cast-item-characters-link"] span::text').getall()
        
        fanal_casts = dict(zip(casts,casts_charcter))
        loader.add_value('casts',fanal_casts)
        
        loader.add_xpath('stars','//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li/a/text()')


        # yield {
        #     'imdb_id':imdb_id,'title':title,"language":language,'casts':fanal_casts,'release_date':release_date,
        #     'cover_url':cover_url,'genres':genres,'description':description,'writers':writers,'director':director,
        #     'country_of_origin':country_of_origin,"run_time":run_time,'rate':rate,'rete_population':rete_population
        #     }
        
        
        yield loader.load_item()
