from os import getenv
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# from sqlalchemy.ext.declarative import declarative_base
# import os
# from decouple import config

load_dotenv()

# db_url = getenv('DB_URL')
# print (db_url)
# DB_URL = "mysql+pymysql://root:Mclaren5@localhost/python_reviews_db"
# connect to database using env variable
# engine = create_engine(db_url, echo=True, pool_size=20, max_overflow=20)

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=20)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)

def get_db():
    if 'db' not in g:
        #store db connections in app context
        g.db = Session()

    return g.db


