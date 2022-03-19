# Salary-Scrapy_Crawler-JSON

### 1. About:

This is a project crawling salary statistics from salary.com using standalone scrapy crawler and JSON.  

The following are the fields that the spider scrapes from the Salary.com

* job_title
* location
* description
* percentile10
* percentile25
* median
* percentile75
* percentile90 

### 2. SalarySpider 
* <b>start_urls</b> - url of the first search page
* <b>parse</b> method -  loading city name to a list, build serch url and send search query for each city
* <b>parse_city</b> method - scaping city search page, extract job statistic info using JSON

### 3. Run the scraper 

        python salarySpider.py 
