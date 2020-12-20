# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class StarspiderPipeline:
    
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('mystars.db')
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS STARS_TB""")
        self.curr.execute("""CREATE TABLE STARS_TB
                          (
                           STAR_ID         text, 
                           STAR_NAME       text, 
                           MAGNITUDE       text,
                           RIGHT_ASCENSION text,
                           DECLINATION     text,
                           LINKS           text
                           )
                         """)
                          
    def process_item(self, item, spider):
        print('Pipeline:' + item['star_id'])
        self.store_db(item)
        return item
    
    def store_db(self, item):
        print('Insert data reached!')
        self.curr.execute("""INSERT INTO STARS_TB VALUES(?,?,?,?,?,?)""",
                           (
                            item['star_id'],
                            item['star_name'],
                            item['magnitude'],
                            item['right_ascension'],
                            item['declination'],
                            item['links']
                            )
                         )
        
        self.conn.commit()
