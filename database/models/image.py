from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP, nullable=False)
    url = Column(String, nullable=False)
