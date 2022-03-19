"""
    Indeed.com Web scraper
    Modified:  2022-02-20
    Author:    Zhigang Nan
"""

import scrapy
from datetime import datetime
from indeed.items import IndeedItem

position = "senior+accountant"
location = 'charlotte+nc'

def get_url(position, location):
    """Generate url from position and location"""
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url

class IndeedSpider(scrapy.Spider):
    name = 'indeedSpider'
    allowed_domains = ['indeed.com']

    start_urls = [get_url(position, location)]

    def parse(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))

        cards = response.css('div[id="mosaic-provider-jobcards"]>a')
            
        for card in cards:
       
            job_title = card.css('h2 > span::text').extract_first()
            
            try:
                company = card.css('span[class="companyName"]::text').extract_first()
            except:
                pass

            if not company :
                try:
                    company = card.css('span[class="companyName"]>a::text').extract_first()
                except :
                    pass

            location = card.css('div[class="companyLocation"]::text').extract()
            location =  ' '.join(location)
            
            post_date = card.css('span[class="date"]::text').extract_first()
            
            extract_date = datetime.today().strftime('%Y-%m-%d')
            
            job_url =  card.css('::attr(href)').extract()
            job_url ='https://www.indeed.com'  + "".join(job_url)
    
            summary = card.css('div[class="job-snippet"] > ul > li ::text').extract()
            summary =  ''.join(summary)
            
            item = IndeedItem()
            item['job_title'] = job_title 
            item['company'] = company 
            item['location'] = location 
            item['post_date'] = post_date                         
            item['extract_date'] = extract_date 
            item['summary'] = summary 
            item['job_url'] = job_url 
                        
            yield item

        try: 
            next_page = response.xpath('.//a[contains(@aria-label, "Next")]/@href').extract_first()

            if next_page is not None:
                next_page = "https://www.indeed.com" + next_page
                yield response.follow(next_page, callback=self.parse)
        except:
            self.logger.info('No Next Page')
            pass  
                    
