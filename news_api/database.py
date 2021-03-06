from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column


engine = create_engine('postgresql://postgres:postgres@db/news_db')
Session = sessionmaker(bind=engine)
session = Session()


class News(Base):   
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    text = Column(String)
    pub_date = Column(String)
    image = Column(String)
