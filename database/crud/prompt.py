from typing import List, Optional
from sqlalchemy.orm import Session

from database.models import Prompt
from database.schemas import PromptSchema


# Prompts CRUD operations
def create_prompt(db: Session, prompt: PromptSchema) -> PromptSchema:
    db_prompt = Prompt(**prompt.dict())
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt

def get_prompt(db: Session, prompt_id: int) -> Optional[PromptSchema]:
    return db.query(Prompt).filter(Prompt.id == prompt_id).first()


def get_prompts(db: Session, skip: int = 0, limit: int = 100) -> List[PromptSchema]:
    return db.query(Prompt).offset(skip).limit(limit).all()

# Custom CRUD for solution
def get_next_unloaded_prompts(db: Session) -> List[PromptSchema]:
    """ returns all unloaded prompts in the order they were created"""
    return db.query(Prompt).filter(Prompt.flg_loaded == False).order_by(Prompt.created_at.asc()).first()

def update_prompt(db: Session, prompt_id: int, prompt: PromptSchema) -> Optional[PromptSchema]:
    db_prompt = get_prompt(db, prompt_id=prompt_id)
    if db_prompt:
        for key, value in prompt.dict().items():
            setattr(db_prompt, key, value)
        db.commit()
        db.refresh(db_prompt)
        return db_prompt


def delete_prompt(db: Session, prompt_id: int) -> Optional[PromptSchema]:
    db_prompt = get_prompt(db, prompt_id=prompt_id)
    if db_prompt:
        db.delete(db_prompt)
        db.commit()
        return db_prompt