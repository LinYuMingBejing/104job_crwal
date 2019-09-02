# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job104CrawlItem(scrapy.Item):
    jobtitle = scrapy.Field()
    companyName = scrapy.Field()
    jobContent = scrapy.Field()
    address = scrapy.Field()
    jobtool = scrapy.Field()
    jobrequirement = scrapy.Field()
    graduaterequirement = scrapy.Field()
    subjectrequirement = scrapy.Field()
    updatetime = scrapy.Field()
    pass
