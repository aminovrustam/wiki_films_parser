# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class ScrwikiPipeline:      
    def __init__(self):
        self.films = []
    
    def process_item(self, film, spider):
        self.films.append(dict(film))
        return film
    
    def close_spider(self, spider):
        df = pd.DataFrame(self.films)
        df.to_csv('output.csv', index=False, encoding='utf-8')
    

