from fastapi import APIRouter
from app.discord.bot_request_templates import MidJourneyRequestTemplate
from app.discord.config import discord_url
from pydantic import BaseModel
import requests

# Initialize the FastAPI app
router = APIRouter()

# Define a dictionary to store the chats
chats = {}
 
# Define the request body schema
class ImagineRequest(BaseModel):
    prompt: str

@router.post("/imagine")
async def chat(request: ImagineRequest):
    payload = MidJourneyRequestTemplate.parse_imagine_template(request.prompt)
    header = MidJourneyRequestTemplate.get_headers()
    response = requests.post(discord_url, json = payload, headers = header)
    return response