from fastapi import APIRouter, Depends
from app.discord.bot_request_templates import MidJourneyRequestTemplate
from app.core.config import DISCORD
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from database.schemas import PromptSchema
from database.crud import create_prompt
import requests
from datetime import datetime

# Initialize the FastAPI app
router = APIRouter()

# Define a dictionary to store the chats
chats = {}
 
# Define the request body schema
class ImagineRequest(BaseModel):
    prompt: str

@router.post("/imagine")
async def chat(request: ImagineRequest, db: Session = Depends(get_db)):
    payload = MidJourneyRequestTemplate.parse_imagine_template(request.prompt)
    header = MidJourneyRequestTemplate.get_headers()
    response = requests.post(DISCORD.url, json = payload, headers = header)
    # Create an instance of the Prompt model
    timestamp = datetime.now()
    prompt_data = PromptSchema(
        created_at = timestamp,
        prompt = request.prompt,
        flg_loaded  = False,
        uploaded_at = timestamp
    )
    create_prompt(db=db, prompt=prompt_data)
    return response