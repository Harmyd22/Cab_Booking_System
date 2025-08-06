from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine
from .Utils.config import Database_url


Base=declarative_base()
engine = create_engine(Database_url)
Sessionlocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        

