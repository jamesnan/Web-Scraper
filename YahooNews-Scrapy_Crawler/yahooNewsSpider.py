"""
    Yahoo News Web scraper
    Modified:  2022-02-20
    Author:    Zhigang Nan
"""

import os
import scrapy
from scrapy.crawler import CrawlerProcess

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'
}

keywords = 'iphone+12'

def get_url(keywords):
    template = 'https://news.search.yahoo.com/search?p={}'
    url = template.format(keywords)
    return url 

class YahooNewsSpider(scrapy.Spider):
    name = 'YahooNewsSpider'
    allowed_domains = ['news.search.yahoo.com']
    
    custom_settings = {'FEEDS': {'yahooNews.csv': {'format': 'csv'}}}
    
    start_urls = [get_url(keywords)]

    def parse(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))

        cards = response.xpath('//div[contains(@class,"NewsArticle")]')

        for card in cards:
            self.logger.info('Got card {}'.format(card)) 
    
            headline = card.xpath('.//h4[contains(@class,"s-title")]/a/text()').getall()
            headline  = "".join(headline).strip()
            source = card.xpath('.//span[contains(@class,"s-source")]/text()').extract()
       
            posted = card.xpath('.//span[contains(@class,"s-time")]/text()').extract()
            posted  = "".join(posted)
            posted = posted.replace('·', '').strip()
     
            description = card.css('p.s-desc::text').extract()
            description  = "".join(description)
     
            link = card.css('a::attr(href)').get()
             
            yield {"headline":headline,"source":source,"posted":posted,"description":description,"link":link}
        
        try: 
            next_page = response.css('a.next').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except:
            pass  


if __name__ == '__main__':
    if os.path.exists("././yahooNews.csv"):
          os.remove("././yahooNews.csv")

    # run scraper
    process = CrawlerProcess()
    process.crawl(YahooNewsSpider)
    process.start()                      






    