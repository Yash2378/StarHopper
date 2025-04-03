from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update this with your actual DB connection string
DATABASE_URL = "postgresql://username:password@localhost/starhopper_db"
# e.g., "mysql+pymysql://username:password@localhost:3306/starhopper_db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL statements
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
