# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PromodbScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome = scrapy.Field()
    preco = scrapy.Field()
    link = scrapy.Field()
    loja = scrapy.Field()

    pass
