from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('postgresql://postgres:master@localhost:5432/traingram', echo=True)
Base.metadata.create_all(engine)
Session_maker = sessionmaker(bind=engine)


class SingletonSession:
   _instance = None

   def __new__(cls):
      if cls._instance is None:
         cls._instance = super().__new__(cls)
      return cls._instance

   def __init__(self):
      self.session = Session_maker()

   def execute(self, stmt):
       return self.session.execute(stmt)


session = SingletonSession()
