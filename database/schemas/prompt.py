from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# Pydantic schema for the Prompt model
class PromptSchema(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    prompt: Optional[str]
    flg_loaded: Optional[bool]
    uploaded_at: Optional[datetime]

    class Config:
        orm_mode = True