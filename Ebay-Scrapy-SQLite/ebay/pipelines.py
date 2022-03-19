# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
con = None

class EbayPipeline(object):
    def __init__(self):
        print ("init EbayPipeline")

        self.con = sqlite3.connect('ebay.db')
        self.cur = self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS Ebay")
        self.createTables()

    def createTables(self):
        print("createTables")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS \
            Ebay(id INTEGER PRIMARY KEY AUTOINCREMENT,\
            title TEXT, \
            rating TEXT, \
            item_price TEXT, \
            item_link TEXT \
            )""")

    def process_item(self, item, spider):
        print("process_item")
        self.cur.execute("INSERT INTO Ebay (title, rating, item_price,item_link) \
            VALUES (?,?,?,?)",\
            (item['title'],item['rating'],item['item_price'],item['item_link'])
        )
        self.con.commit()

        print('------------------------')
        print('Data Stored in Database')
        print('------------------------')
        return item

