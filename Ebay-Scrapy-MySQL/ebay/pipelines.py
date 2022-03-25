# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sys
import mysql.connector
from mysql.connector import errorcode
from itemadapter import ItemAdapter

con = None

class EbayPipeline(object):
    def __init__(self):
        print ("init EbayPipeline")
        self.create_conn()
        self.create_table()
        
    def create_conn(self):
        # connect to Connect to DB
        try:
            self.con = mysql.connector.connect(
                                    user = 'user',
                                    password = 'password',
                                    host = 'localhost',
                                    port=3306,
                                    database = 'ebay'
                                    )
        except mysql.error as e:
            print(f"Error connecting to DB platform : {e}")
            sys.exit(1)

        self.cur = self.con.cursor()
        
        
    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS Ebay""")
        print("createTables")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS \
            Ebay(id INT AUTO_INCREMENT PRIMARY KEY,\
            title  VARCHAR(255), \
            rating  VARCHAR(255), \
            item_price  VARCHAR(255), \
            item_link  VARCHAR(1024) \
            )""")
            
    def process_item(self, item, spider):
        print("process_item")
        myquery = """INSERT into ebay
        (
        title ,
        rating,
        item_price,
        item_link
        )
        values (%s,%s,%s,%s)
        """
        val=(
        item.get('title'),
        item.get('rating'),
        item.get('item_price'),
        item.get('item_link')
        )
        self.cur.execute(myquery,val)
                
        self.con.commit()

        print('------------------------')
        print('Data Stored in Database')
        print('------------------------')
        return item

    def close_spider(self, spider):
        self.con.close()