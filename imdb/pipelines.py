# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, SimpleStatement


class ImdbPipeline:
    def __init__(self):
        cluster = Cluster(['localhost'], port=9042)
        self.session = cluster.connect()
        self.create_keyspace()
        self.create_table()
        self.batch = BatchStatement()

    def create_keyspace(self):
        self.session.execute(
            "CREATE KEYSPACE IF NOT EXISTS imdb_crawler WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};"
        )
        self.session.execute(
            "USE imdb_crawler "
        )

    def create_table(self):
        self.session.execute(
            """CREATE TABLE IF NOT EXISTS imdb(
                imdb_id text PRIMARY KEY,
                title text,
                release_date text,
                cover_url text,
                genres list<text>,
                description text,
                director list<text>,
                writers list<text>,
                country_of_origin text,
                language list<text>,
                run_time text,
                rate text,
                rete_population text,
                casts map<text, text>,
                stars list<text>,
                film_location list<text>,
                budget text,
                color text,
                sound_mix list<text>,
                aspect_ratio text,
                production_companies list<text>,
                oscars text,
                awards text
                );"""
        )

    def process_item(self, item, spider):
        batch = self.batch.add(
            SimpleStatement("""INSERT INTO imdb(
            imdb_id,title,release_date,cover_url,genres,
            description,director,writers,country_of_origin,language,
            run_time,rate,rete_population,casts,stars,film_location,budget,
            color,sound_mix,aspect_ratio,production_companies,oscars,awards            
            ) values (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s)"""),
            (
                item['imdb_id'],
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
                item['rete_population'],
                item['casts'],
                item['stars'],
                item['film_location'],
                item['budget'],
                item['color'],
                item['sound_mix'],
                item['aspect_ratio'],
                item['production_companies'],
                item['oscars'],
                item['awards'],
            ))

        self.session.execute(batch)

        return item
