from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database import Base
class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP, nullable=False)
    prompt = Column(String, nullable=False)
    flg_loaded = Column(Boolean, nullable=False)
    uploaded_at = Column(TIMESTAMP, nullable=True)
