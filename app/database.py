from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import time
import os

load_dotenv()


DATABASE_URL =os.getenv("DATABASE_URL","sqlite:///./ban.bd")


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False} if "sqlite" in DATABASE_URL else {})

SenssionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SenssionLocal()
    try:
        yield db
    finally:
        db.close()