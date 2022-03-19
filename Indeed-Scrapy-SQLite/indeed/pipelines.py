# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import sqlite3
# from itemadapter import ItemAdapter

con = None

class IndeedPipeline(object):
    def __init__(self):
        print ("init IndeedPipeline")

        self.con = sqlite3.connect('indeed.db')
        self.cur = self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS Indeed")
        self.createTables()

    def createTables(self):
        print("createTables")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Indeed 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT, 
            company TEXT, 
            location TEXT, 
            post_date TEXT, 
            extract_date TEXT,   
            summary TEXT,                     
            job_url TEXT 
            )""")

    def process_item(self, item, spider):
        print("process_item")
        self.cur.execute("INSERT INTO Indeed \
            (job_title, company, location,post_date,extract_date,summary,job_url) \
            VALUES (?,?,?,?,?,?,?)",\
            (item['job_title'], \
             item['company'],\
             item['location'],\
             item['post_date'],\
             item['extract_date'],\
             item['summary'] ,  \
             item['job_url'])
        )
        self.con.commit()

        print('------------------------')
        print('Data Stored in Database')
        print('------------------------')
        # return item              