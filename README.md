# tg-bot

Телеграм-бот, который призван помочь художникам в поиске идей для рисования.

На данный момент доступны 2 функции:
1. Найти красивую фотографию по запросу пользователя - бот использует api сайта pexels.com, находит нужное фото и присылает его. Можно получить несколько картинок по одному запросу.
2. Бот присылает 3-х животных для челенджа Random Creature Design - художник должен нарисовать существо, имеющее характерные черты присланных зверей. (Например, грифон имеет черты льва и орла). Для осуществления этой функции бот собирает с сайта https://kupidonia.ru/spisok/spisok-zhivotnyh алфавитный перечень животных с помощью BeautifulSoup, выбирает из списка 3-х животных, а затем присылает пользователю названия и картинки-референсы этих животных - картинки находятся с помощью Google-Image-Search

Несмотря на то, что оба api глобально предназначены для поиска картинок, использовать какое-то одно из них было бы неразумно: pexels предоставляет красивые картинки по запросу, в отличие от google, которые больше подходят для использования в качестве референса, но при этом там нельзя найти каких-то специфичных животных, которые как раз встречаются во второй функции, поэтому там использован поиск от google. 
