# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitterItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field()
    twitter_id = scrapy.Field()
    text = scrapy.Field()
    pass
