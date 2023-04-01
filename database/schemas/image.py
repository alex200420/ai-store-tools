from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# Pydantic schema for the Image model
class ImageSchema(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    url: Optional[str]

    class Config:
        orm_mode = True



