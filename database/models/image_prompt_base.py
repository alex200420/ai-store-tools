from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from database import Base

class ImagePromptBase(Base):
    __tablename__ = "image_prompt_base"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    prompt_id = Column(Integer, ForeignKey("prompts.id"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
