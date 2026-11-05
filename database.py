from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:monpostgres46@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autoflush=False, bind=engine)

def get_db():
    with SessionLocal() as db:
        yield db