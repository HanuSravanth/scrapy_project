# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StarspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    star_id         = scrapy.Field()
    star_name       = scrapy.Field()
    magnitude       = scrapy.Field()
    right_ascension = scrapy.Field()
    declination     = scrapy.Field()
    links           = scrapy.Field()

