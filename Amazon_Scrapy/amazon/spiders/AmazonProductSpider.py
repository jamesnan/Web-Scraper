"""
    Amazon.com Web scraper
    Modified:  2022-03-18
    Author:    Zhigang Nan
"""
import scrapy
from time import sleep
from random import randint
from amazon.items import AmazonItem

search_term = "iphone 13"

def get_url(search_term, page):
    base_template = 'https://www.amazon.com/s?k={}'
    search_term = search_term.replace(' ', '+')
    url = base_template.format(search_term)
    if page >1:
         url += ('&page=' + str(page))
    return url

class AmazonProductSpider(scrapy.Spider):
    name = 'AmazonProductSpider'
    allowed_domains = ["amazon.com"]
   
    start_urls = [get_url(search_term, 1)]

    def parse(self, response):

        products = response.css('div[data-component-type="s-search-result"]')

        for product in products:
            description = product.css('h2 > a > span::text').extract()
            price = product.css('span[class="a-offscreen"]::text').extract()
            url = 'https://www.amazon.com' + product.css('h2 > a::attr(href)').extract_first()
            rating = product.xpath('.//span[contains(@aria-label, "out of")]/@aria-label').extract_first()
            review_count = product.xpath('.//span[contains(@aria-label, "out of")]/following-sibling::span/@aria-label').extract_first()
            
            yield {'description': description, 'price':price, 'rating':rating, 'review_count':review_count, 'url':url}

        try: 
            next_page =  response.xpath('.//a[contains(@aria-label, "Go to next page")]/@href').extract_first()
            if next_page is not None:
                next_page = 'https://www.amazon.com' + next_page
                yield response.follow(next_page, callback=self.parse)
        except:
            pass  
        

            
