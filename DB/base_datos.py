from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
class Database:
    def __init__(self):
        self.database_url = 'mysql+pymysql://root:root@localhost/nexticket'
        self.engine = create_engine(self.database_url)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_session(self):
        return self.session

db = Database()