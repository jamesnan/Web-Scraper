# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class IndeedItem(Item):

    job_title = Field()
    company = Field()
    location = Field()
    post_date = Field()
    extract_date = Field()
    summary = Field()
    job_url = Field()
