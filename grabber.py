import os
from dotenv import load_dotenv
load_dotenv()
import feedparser


class Grabber:
    """ 
    - get_news(channel -> int, limit -> int)
        channel:
            0 - Lenta
            1 - Interfax
            2 - Kommersant
            3 - m24
        limit - количество новостей, которые попадут в выборку

    - get_all_news(limit -> int)
        Получает новости со всех каналов
        limit - количество новостей, которые попадут в выборку
    """
    def __init__(self):
        self.urls = [
            os.environ.get('LENTA_URL'),
            os.environ.get('INTERFAX_URL'),
            os.environ.get('KOMMERSANT_URL'),
            os.environ.get('M24_URL')
        ] 

    def get_news(self, channel, limit):
        url = self.urls[channel]
        feed = feedparser.parse(url)
        all_data = feed["items"]
        news = []
        for event in all_data:
            if limit > 0:
                item = {}
                item['title'] = event['title']
                item['link'] = event['link']
                item['text'] = event['description']
                item['pub_date'] = event['published']
                if channel == 0 or channel == 3:
                    item['image'] = event['links'][1]['href']
                news.append(item)
                limit -= 1
            else:    
                return news                 

    def get_all_news(self, limit):
        all_news = []
        for channel in range(0,4):
            all_news.append(self.get_news(channel, limit))
        return all_news



if __name__ == '__main__':
    limit = 3
    channel = 3
    grabber = Grabber()
    #print(grabber.get_news(channel, limit))
    print(grabber.get_all_news(limit))
