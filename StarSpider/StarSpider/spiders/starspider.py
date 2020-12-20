import scrapy
from ..items import StarspiderItem

class StarspiderSpider(scrapy.Spider):
    name = 'starspider'
    allowed_domains = ['https://star-register.org/']
    start_urls = ['http://star-register.org//']
    page_offset = 24

    def parse(self, response):
        
        items = StarspiderItem()
        all_stars = response.css('a.item')
        
        for star in all_stars:
            star_id         = star.css('div:nth-child(1)::text').extract()[0]
            star_name       = response.css('strong::text').extract()[all_stars.index(star)]
            magnitude       = star.css('div:nth-child(3)::text').extract()[0].replace('Magnitude: ','')
            right_ascension = star.css('div:nth-child(4)::text').extract()[0].split(',')[0].replace('RA: ','')
            declination     = star.css('div:nth-child(4)::text').extract()[0].split(',')[1].replace(' DEC: ','')
            links           = star.css('img.image::attr(src)').extract()[0]
            
            items['star_id']         = star_id
            items['star_name']       = star_name
            items['magnitude']       = magnitude
            items['right_ascension'] = right_ascension
            items['declination']     = declination
            items['links']           = links
            
            yield items

        # https://star-register.org/?offset=12&search=
    
        next_page = 'https://star-register.org/?offset='+str(StarspiderSpider.page_offset)+'&search='
        
        if StarspiderSpider.page_offset < 100:
            print('offset: ',StarspiderSpider.page_offset)
            yield response.follow(next_page, callback = self.parse)
            StarspiderSpider.page_offset += 12