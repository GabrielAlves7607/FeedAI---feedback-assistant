from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./feedbacks.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedbacks"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    feedback_type = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)
