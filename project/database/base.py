from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from project.config import db_url

class Base(DeclarativeBase):
    pass


engine = create_engine(db_url)
session_factory = sessionmaker(bind=engine)
session = session_factory()


def get_session() -> Session:
    return session


def close_session():
    session.close()
