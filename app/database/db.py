from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from utils import load_env

load_env()

user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
endpoint = os.environ["DB_ENDPOINT"]
database = os.environ["DB_NAME"]
port = os.environ["DB_PORT"]

url_obj = URL.create(
    drivername="postgresql+psycopg2",
    username=user,
    password=password,
    host=endpoint,
    port=int(port),
    database=database,
)

engine = create_engine(url=url_obj)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
