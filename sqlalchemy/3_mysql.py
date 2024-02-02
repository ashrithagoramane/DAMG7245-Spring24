import warnings
warnings.filterwarnings("ignore")

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import bcrypt
import os

load_dotenv()

DB_USERNAME = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DATABASE = os.getenv("MYSQL_DATABASE")
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.id} {self.username} {self.hashed_password}"

Base.metadata.create_all(bind=engine)

factory = sessionmaker(bind = engine)
session = factory()

def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())    
    db_user = User(username=username, hashed_password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_user_by_username(username: str):
    return session.query(User).filter(User.username == username).first()


print("Creating user" , create_user("dummy", "dummy"))
print("Get user by username (dummy)", get_user_by_username("dummy"))
