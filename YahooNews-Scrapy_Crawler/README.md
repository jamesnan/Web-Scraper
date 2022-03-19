# YahooNews-Scrapy_Crawler

### 1. About:

This is a project crawling Yahoo News article from Yahoo using standalone scrapy crawler, and saving data to csv file.

The following are the fields the spider scrapes from the Salary.com

* headline
* source
* posted
* description
* link

### 2. YahooNewsSpider Class
* <b>start_urls</b> - url of the first search page
* <b>parse</b> method - scraping Yahoo News article from search page and then navigate to next page with callback

### 3. Run the scraper 

        python YahooNewsSpider.py 
