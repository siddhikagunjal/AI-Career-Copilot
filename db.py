from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://Z4BZCLgL8XAXLXh.root:rjb1VHKiVydmBC0s@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()