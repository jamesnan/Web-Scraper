# Indeed-Scrapy-SQLite

### 1. About:

This is a project crawling Job postings from Indeed.com using python scrapy and saving data to sqlite database. The following are the fields the spider scrapes from the indeed job posting page:

* job_title 
* company 
* location 
* post_date                         
* extract_date 
* summary 
* job_url 

### 2. IndeedSpider Class
* <b>start_urls</b> - url of the first search page
* <b>parse</b> - scraping job data of the search page and then navigate to next page with callback

### 3. IndeedPipeline class

    After scraping data, scrapy calls IndeedPipeline class to process data and save them to a SQLite database.
 
### 4. Run the scraper 
     scrapy crawl indeedSpider


