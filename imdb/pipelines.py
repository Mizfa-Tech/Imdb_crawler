# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from clickhouse_driver import Client


class ImdbPipeline:
    def __init__(self):
        self.db = Client(host='localhost', port=19000)
        self.create_database()
        self.create_table()
        
    def create_database(self):
        self.db.execute(
        "CREATE DATABASE IF NOT EXISTS imdb;"
        )
        
    def create_table(self):
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS imdb.information(
                imdb_id String,
                title String,
                release_date String,
                cover_url String,
                genres Array(String),
                description String,
                director Array(String),
                writers Array(String),
                country_of_origin String,
                language Array(String),
                run_time String,
                rate String,
                rete_population String,
                casts Map(String,String),
                stars Array(String),
            )ENGINE=MergeTree() PRIMARY KEY(imdb_id) SETTINGS insex_grabularity=8192;
            """
        
            
        )
    
    def process_item(self, item, spider):
        self.db.execute(
            """INSERT INTO imdb.information values""",
            [(item['imdb_id'],
                item['title'],
                item['release_date'],
                item['cover_url'],
                item['genres'],
                item['description'],
                item['director'],
                item['writers'],
                item['country_of_origin'],
                item['language'],
                item['run_time'],
                item['rate'],
                item["rete_population"],
                item['casts'],
                item['stars'],
            )]
        )
        
        

        return item
