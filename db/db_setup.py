from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://roro:Ubuntu_passq1w2e3r4t5@localhost/fast_lms"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()


# DB utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

