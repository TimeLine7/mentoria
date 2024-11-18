from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

SQLALCHEMY_DATABASE_URL = "sqlite:///ban.bd"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SenssionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)
Base = declarative_base()

connected = False
while not connected:
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        connected = True
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        time.sleep(5)
def get_db():
    db = SenssionLocal()
    try:
        yield db
    finally:
        db.close()