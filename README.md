# wiki_films_parser
## Wiki parser using scrapy

Парсер был написан на языке python, используя библиотеку scrapy.

Парсер начинает с данной страницы википедии https://ru.wikipedia.org/wiki/Категория_по_фильмам и идет далее, заходя на страницу каждого фильма и собирая информацию о нем (title, genre, director, country, year)
Далее программа сохраняет полученную информацию в csv файл.
