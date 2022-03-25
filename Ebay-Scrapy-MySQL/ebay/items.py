# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class EbayItem(Item):
    # define the fields for your item here like:
    title = Field()
    rating = Field()
    item_price = Field()
    item_link = Field()