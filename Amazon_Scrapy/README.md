# Amazon-Scrapy-Scraper 

## About:

  Python Scrapy spider that searches Amazon by keywords, collects product infomation, and outputs data to csv file. The spider will iterate pages returned by the keyword query. The following are the fields the spider scrapes from the Amazon product search page:

  * description
  * price 
  * rating 
  * review count 
  * product url
            
## Using the Scrapy Spider

### 1. Make sure Scrapy is installed:
```
pip install scrapy
```
  
### 2. Get started with project
```
scrapy startproject amazon
```
### 3. Create Spiders
```
scrapy genspider AmazonProductSpider amazon
```

The above steps will create a dirctory structure with following contents:
```
../
  scrapy.cfg
  amazon/
       __init__.py
      items.py
      pipelines.py
      settings.py
      spiders/
          AmazonProductSpider.py
           __init__.py
```

### 4. Edit AmazonProductSpider 

* <b>start_urls</b> - url of the first search page
* <b>parse</b> - scraping product data from the search page and then navigate to next page with callback.

### 5. Run the scraper to collect data and output data to a csv file
    scrapy crawl AmazonSpider -o items.csv

## Reference
https://www.blog.datahut.co/post/tutorial-how-to-scrape-amazon-data-using-python-scrapy

