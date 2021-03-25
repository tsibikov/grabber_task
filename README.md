# Граббер статей с новостных сайтов:

- http://lenta.ru/rss
- http://www.interfax.ru/rss.asp
- http://www.kommersant.ru/RSS/news.xml
- http://www.m24.ru/rss.xml

### grabber.py:

 - Реализован базовый функционал 

### news_api:

 - API доступно по адресу http://188.225.34.220:8000/docs

### Разворачивание проекта через docker

 - Склонировать репозиторий

 - Создать файл .env по образцу

    - LENTA_URL=http://lenta.ru/rss
    - INTERFAX_URL=https://www.interfax.ru/rss.asp
    - KOMMERSANT_URL=https://www.kommersant.ru/RSS/news.xml
    - M24_URL=https://www.m24.ru/rss.xml
    - POSTGRES_USER=postgres 
    - POSTGRES_PASSWORD=postgres
    - POSTGRES_DB=news_db

 - docker-compose build

 - docker-compose up -d

Проект доступен на localhost:8000/get-news/
  

