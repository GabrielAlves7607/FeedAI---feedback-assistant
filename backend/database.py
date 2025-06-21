from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database URL
DATABASE_URL = "sqlite:///./feedbacks.db"

# SQLAlchemy engine and session setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Feedback table model
class Feedback(Base):
    __tablename__ = "feedbacks"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    feedback_type = Column(String, nullable=False)

# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
