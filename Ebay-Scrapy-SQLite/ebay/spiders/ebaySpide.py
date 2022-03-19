"""
    Ebay Web scraper
    Modified:  2022-03-18
    Author:    Zhigang Nan
"""

from ebay.items import EbayItem
import scrapy

keywords = "iphone+13"

def get_url(keywords, page):
    base_template = 'https://www.ebay.com/sch/i.html?_=&_nkw={}&_ipg=240'
    url = base_template.format(keywords) + ('&_pgn=' + str(page))
    return url

class EbaySpider(scrapy.Spider):
    name = 'ebaySpider'
    allowed_domains = ['ebay.com']

    start_urls = [get_url(keywords, 1)]

    def parse(self, response):

        self.logger.info('Got successful response from {}'.format(response.url))

        products = response.css("ul[class='srp-results srp-list clearfix']>li")
        
        for product in products:
            self.logger.info('Got product : {}'.format(product))

            try:
                title = product.css("h3::text").extract()
                title = ''.join(title).strip()
            except Exception as e:
                title =-1

            try:
                rating = product.css( 'div[class="x-star-rating"] > span[class="clipped"]::text').extract_first()
            except Exception as e:
                rating =-1
            
            try:
                item_price = product.css("span[class='s-item__price']::text").extract_first()
            except Exception as e:
                item_price = -1
                
            try:
                item_link = product.css("a[class='s-item__link']::attr(href)").extract_first()
            except Exception as e:
                item_link = -1

            item = EbayItem()
            item["title"] = title 
            item["rating"] = rating
            item["item_price"] = item_price 
            item["item_link"] = item_link 
            yield item

        try: 
            next_page = next_page = response.xpath('.//a[contains(@aria-label, "Go to next search page")]/@href').extract_first()

            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except:
            pass  
        


