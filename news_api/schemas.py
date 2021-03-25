from pydantic import BaseModel
from typing import List


class News_schema(BaseModel):
    title: str
    link: str
    text: str
    pub_date: str
    image: str


class AllNews_schema(BaseModel):
    all_news: List[News_schema]
