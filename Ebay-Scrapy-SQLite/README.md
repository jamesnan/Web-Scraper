# Ebay-Scrapy-SQLite

### 1. About:

This is a project crawling ebay product information from ebay.com using python scrapy and saving data to a sqlite database. The following are the fields the spider scrapes from the ebay search page:

* title 
* rating
* item_price 
* item_link 

### 2. EbaySpider class
* <b>start_urls</b> -  url of the first search page
* <b>parse</b> method - scraping product data from the search page and then navigate to next page with callback

### 3. EbayPipeline class

    After scraping data, scrapy calls EbayPipeline class to process data and save them to SQLite database.
 
### 4. Run the scraper
     scrapy crawl ebaySpider


