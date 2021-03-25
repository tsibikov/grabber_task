from fastapi import FastAPI
import os
from sqlalchemy.orm import Session
from dotenv import load_dotenv
load_dotenv()
import feedparser
from schemas import AllNews_schema, News_schema
from database import session, News

app = FastAPI()


@app.get('/get-news')
def get_response():
    get_all_news()
    news_query = session.query(News).order_by(News.id.desc()).limit(12)
    session.close()
    news = []
    for item in news_query:
        news_item = News_schema(
            title=item.title,
            link=item.link,
            text=item.text,
            pub_date=item.pub_date,
            image=item.image
        )
        news.append(news_item)
    all_news = AllNews_schema(all_news=news)
    return str(all_news.dict())


def get_all_news():
    for channel in range(0,4):
        get_news(channel)


def get_news(channel: int):
    urls = [
        os.environ.get('LENTA_URL'),
        os.environ.get('INTERFAX_URL'),
        os.environ.get('KOMMERSANT_URL'),
        os.environ.get('M24_URL')
    ]
    limit = 3
    feed = feedparser.parse(urls[channel])
    all_data = feed["items"]
    for event in all_data:
        if limit > 0:
            title = event['title']
            link = event['link']
            text = event['description']
            pub_date = event['published']
            if channel == 0 or channel == 3:
                image = event['links'][1]['href']
            else:
                image = 'no image'      
            news = News(title=title, 
                    link=link, 
                    text=text, 
                    pub_date=pub_date, 
                    image=image)
            session.add(news)      
            session.commit()
            limit -= 1
        else:   
            session.close() 
            return 
