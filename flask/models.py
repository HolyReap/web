import atexit
import os

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

PG_USER = os.getenv("PG_USER", "user")
PG_PASSWORD = os.getenv("PG_PASSWORD", "1111")
PG_DB = os.getenv("PG_DB", "flaskhw")
PG_HOST = os.getenv("PG_HOST","127.0.0.1")
PG_PORT = os.getenv("PG_PORT","5431")

PG_DSN = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_engine(PG_DSN)
atexit.register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = "app_users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    
class Advertisement(Base):
    __tablename__ = "advertisments"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(ForeignKey("app_users.id", ondelete="CASCADE"))
    
Base.metadata.create_all()