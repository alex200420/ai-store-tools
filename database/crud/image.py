from typing import List, Optional
from sqlalchemy.orm import Session

from database.models import Image
from database.schemas import ImageSchema

# Images CRUD Operations
def create_image(db: Session, image: ImageSchema) -> ImageSchema:
    db_image = Image(created_at=image.created_at, url=image.url)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_image(db: Session, image_id: int) -> Optional[ImageSchema]:
    return db.query(Image).filter(Image.id == image_id).first()


def get_images(db: Session, skip: int = 0, limit: int = 100) -> List[ImageSchema]:
    return db.query(Image).offset(skip).limit(limit).all()
    

def update_image(db: Session, image_id: int, image: ImageSchema) -> Optional[ImageSchema]:
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if db_image:
        for key, value in image.dict().items():
            setattr(db_image, key, value)
        db.commit()
        db.refresh(db_image)
        return db_image


def delete_image(db: Session, image_id: int) -> Optional[ImageSchema]:
    db_prompt = get_image(db, prompt_id=image_id)
    if db_prompt:
        db.delete(db_prompt)
        db.commit()
        return db_prompt
