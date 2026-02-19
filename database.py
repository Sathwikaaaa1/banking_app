import os
from sqlalchemy import create_engine 	#manager
from sqlalchemy.ext.declarative import declarative_base 	#blueprint maker - python classes to db table
from sqlalchemy.orm import sessionmaker #it handles opening and closing of conversations with db


SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:password@localhost:5432/bank_db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

#each instance of this class is a db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#we will inherit from this class to be a db session
Base = declarative_base()

#creates a new session for each request and closes it
def get_db():  #generator gives each user their own temporary conversation with the database
    db = SessionLocal()
    try:
        yield db 	#api function ki db connection
    finally:
        db.close()