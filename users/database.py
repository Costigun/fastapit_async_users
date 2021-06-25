from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_DATABASE_URL = 'postgresql://maksim:deathless33@db:5432/users'

engine = create_engine(SQL_DATABASE_URL,echo=True,)


Sessionlocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()