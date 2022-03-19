"""
    Salary.com Web scraper
    Modified:  2022-02-20
    Author:    Zhigang Nan
"""
import os
import json
import csv
import scrapy
from scrapy.crawler import CrawlerProcess

position = "senior accountant"

def get_city():
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'largest_cities.csv')

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        cities = [city for row in reader for city in row]
    return(cities) 

def get_url(position, city):
    """Generate url from position and location"""
    template = 'https://www.salary.com/research/salary/alternate/{}-salary/{}'
    position = position.replace(' ', '-')
    city = city.replace(' ', '-')
    url = template.format(position, city)
    return url

class SalarySpider(scrapy.Spider):
    name = 'salarySpider'
    allowed_domains = ['salary.com']

    custom_settings = {'FEEDS': {'salary.csv': {'format': 'csv'}}}

    start_urls  = ['https://www.salary.com']

    def parse(self, response):
        
        cities = get_city()

        for city in cities:
            url = get_url(position, city)
            yield scrapy.Request( url , callback=self.parse_city)

    def parse_city(self, response):

        self.logger.info('Got successful response from {}'.format(response.url))

        items = {}

        json_raw = response.css('script[type="application/ld+json"]')[1] 
        json_raw = json_raw.css('::text').get()
        json_data = json.loads(json_raw)

        items['job_title'] = json_data['name']
        items['location'] = json_data['occupationLocation'][0]['name']
        items['description'] = json_data['description']
        items['percentile10'] = json_data['estimatedSalary'][0]['percentile10']
        items['percentile25'] = json_data['estimatedSalary'][0]['percentile25']
        items['median'] = json_data['estimatedSalary'][0]['median']
        items['percentile75'] = json_data['estimatedSalary'][0]['percentile75']
        items['percentile90'] = json_data['estimatedSalary'][0]['percentile90']

        yield items
  
if __name__ == '__main__':
    if os.path.exists("././salary.csv"):
          os.remove("././salary.csv")

    # run scraper
    process = CrawlerProcess()
    process.crawl(SalarySpider)
    process.start()








    