from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

SQLALCHEMY_DATABASE_URL = "sqlite:///ban.bd"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SenssionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)
Base = declarative_base()