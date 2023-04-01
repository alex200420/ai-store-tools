from typing import List, Optional
from sqlalchemy.orm import Session

from database.models import ImagePromptBase
from database.schemas import ImagePromptBaseSchema

# ImagePromptBase CRUD operations
def create_image_prompt_base(db: Session, image_prompt_base: ImagePromptBaseSchema) -> ImagePromptBaseSchema:
    db_image_prompt_base = ImagePromptBase(**image_prompt_base.dict())
    db.add(db_image_prompt_base)
    db.commit()
    db.refresh(db_image_prompt_base)
    return db_image_prompt_base

def get_image_prompt_base(db: Session, image_prompt_base_id: int) -> Optional[ImagePromptBaseSchema]:
    return db.query(ImagePromptBase).filter(ImagePromptBase.id == image_prompt_base_id).first()

def get_image_prompt_bases(db: Session, skip: int = 0, limit: int = 100) -> List[ImagePromptBaseSchema]:
    return db.query(ImagePromptBase).offset(skip).limit(limit).all()

def update_image_prompt_base(db: Session, image_prompt_base_id: int, image_prompt_base: ImagePromptBaseSchema) -> Optional[ImagePromptBaseSchema]:
    db_image_prompt_base = get_image_prompt_base(db, image_prompt_base_id=image_prompt_base_id)
    if db_image_prompt_base:
        for key, value in image_prompt_base.dict().items():
            setattr(db_image_prompt_base, key, value)
        db.commit()
        db.refresh(db_image_prompt_base)
        return db_image_prompt_base

def delete_image_prompt_base(db: Session, image_prompt_base_id: int) -> Optional[ImagePromptBaseSchema]:
    db_image_prompt_base = get_image_prompt_base(db, image_prompt_base_id=image_prompt_base_id)
    if db_image_prompt_base:
        db.delete(db_image_prompt_base)
        db.commit()
        return db_image_prompt_base
