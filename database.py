# Versão com SQLite 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./tabelas_banco.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# Versão Original 

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from dotenv import load_dotenv
# import os

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# class Base(DeclarativeBase):
#     pass

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()