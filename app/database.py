from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor 
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# try:
#     conn = psycopg2.connect(host='localhost', database='fastapi', 
#                            user='henock', password='ytmttre883',
#                            cursor_factory = RealDictCursor)
#     cursor = conn.cursor()
#     print("Database was successfully connected")
# except Exception as error:
#     print("Connecting to DB failed")
#     print("Error:", error)