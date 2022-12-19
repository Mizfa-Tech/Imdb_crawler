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
            """
            CREATE TABLE IF NOT EXISTS imdb_link(
                imdb_id text PRIMARY KEY,
                title text,
                );
            """
        )

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
        if spider.name in ['imdb']:
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
                    item.get('imdb_id'),
                    item.get('title'),
                    item.get('release_date'),
                    item.get('cover_url'),
                    item.get('genres'),
                    item.get('description'),
                    item.get('director'),
                    item.get('writers'),
                    item.get('country_of_origin'),
                    item.get('language'),
                    item.get('run_time'),
                    item.get('rate'),
                    item.get('rete_population'),
                    item.get('casts'),
                    item.get('stars'),
                    item.get('film_location'),
                    item.get('budget'),
                    item.get('color'),
                    item.get('sound_mix'),
                    item.get('aspect_ratio'),
                    item.get('production_companies'),
                    item.get('oscars'),
                    item.get('awards'),
                ))

            self.session.execute(batch)

            return item

        elif spider.name in ['link']:
            batch = self.batch.add(
                SimpleStatement(
                    """INSERT INTO imdb_link(imdb_id,title) values (%s,%s)"""),
                (
                    item.get('imdb_id'),
                    item.get('title'),
                ))

            self.session.execute(batch)

            return item

