# -->SQL(Relational) Databases 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False} # for SQLite only (make connection for each threds) 
)
sessinonlocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)  
# bind = engine --> connect each session object, 
Base = declarative_base()  
# use for make new table in the database using the  metadata object in model.py file  class and mapping related fields alse

