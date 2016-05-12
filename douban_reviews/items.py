# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    reviewer = scrapy.Field()
    reviewer_link = scrapy.Field()
    rating_title = scrapy.Field()
    rating = scrapy.Field()
    time = scrapy.Field()
    review_link = scrapy.Field()
    title = scrapy.Field()
    review_short = scrapy.Field()
    review_full = scrapy.Field()
    review_useful = scrapy.Field()
    review_unuseful = scrapy.Field()