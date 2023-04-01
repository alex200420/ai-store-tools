from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# Pydantic schema for the ImagePromptBase model
class ImagePromptBaseSchema(BaseModel):
    id: Optional[int]
    image_id: Optional[int]
    prompt_id: Optional[int]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
