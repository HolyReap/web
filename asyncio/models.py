import atexit
import os

from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PG_USER = os.getenv("PG_USER", "user")
PG_PASSWORD = os.getenv("PG_PASSWORD", "1111")
PG_DB = os.getenv("PG_DB", "async")
PG_HOST = os.getenv("PG_HOST","127.0.0.1")
PG_PORT = os.getenv("PG_PORT","5431")

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_async_engine(PG_DSN)

Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class SwapiCharacters(Base):
    __tablename__ = "swapi_characters"
    
    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_colour = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)
    