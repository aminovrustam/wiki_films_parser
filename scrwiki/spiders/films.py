import scrapy
from scrwiki.items import Films

class FilmsSpider(scrapy.Spider):
    name = "films"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = ["https://ru.wikipedia.org/wiki/Категория:Фильмы_по_алфавиту"]

    def parse(self, response):

        links = response.css('div.mw-category-columns a::attr(href)').getall()

        for link in links:
            url = 'https://ru.wikipedia.org'+str(link)
            yield scrapy.Request(url=url, callback=self.parse_films)

       
        flag1 = response.css('#mw-pages > a:nth-child(6)::text').get()
        flag2 = response.css('#mw-pages > a:nth-child(8)::text').get()
        if flag1 == 'Следующая страница':
            next_page_href = 'https://ru.wikipedia.org' + response.css('#mw-pages > a:nth-child(6)::attr(href)').get()
        elif flag2 == 'Следующая страница':
            next_page_href = 'https://ru.wikipedia.org' + response.css('#mw-pages > a:nth-child(8)::attr(href)').get()

        if flag1 != 'Предыдущая страница':
            yield scrapy.Request(url=next_page_href, callback=self.parse)
    

    def parse_films(self, response):
        for selector in response.css('table.infobox > tbody'):
            film = Films()
            film['title'] = selector.css('th.infobox-above::text').getall()

            film['genre'] = selector.css('span[data-wikidata-property-id="P136"]  a::text, div[data-wikidata-property-id="P136"]  a::text').getall()


            film['director'] = selector.css('span[data-wikidata-property-id="P57"] > a::text, div[data-wikidata-property-id="P57"] > a::text').getall()


            film['country'] = selector.css('a > span.wrap::text').getall()


            if selector.css('a > span.dtstart::text').get() is not None:

                film['year'] = selector.css('a > span.dtstart::text').getall()
            else:

                film['year'] = selector.css('span.nowrap > a::text').getall()
            yield film

