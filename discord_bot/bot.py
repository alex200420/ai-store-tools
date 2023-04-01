import requests
import discord
from discord.ext import commands
import requests
import config as cfg
import logging
from PIL import Image
from config import DISCORD
import os
import re
from utils.cloud_utils import CloudStorage
from database.schemas import ImageSchema, ImagePromptBaseSchema
from database.crud import get_next_unloaded_prompts, create_image, create_image_prompt_base
from database import get_db
from datetime import datetime

logging.basicConfig(filename='myapp.log', level=logging.INFO)

# Create a custom logger
logger = logging.getLogger("discord.bot" if __name__ == '__main__' else "__main__")

client = commands.Bot(command_prefix="*", intents=discord.Intents.all())

cloud_conn = CloudStorage()

db = get_db()

def split_image(image_file):
    """Split an image into four equal parts and return them as a tuple."""
    with Image.open(image_file) as im:
        # Get the width and height of the original image
        width, height = im.size
        # Calculate the middle points along the horizontal and vertical axes
        mid_x = width // 2
        mid_y = height // 2
        # Split the image into four equal parts
        top_left = im.crop((0, 0, mid_x, mid_y))
        top_right = im.crop((mid_x, 0, width, mid_y))
        bottom_left = im.crop((0, mid_y, mid_x, height))
        bottom_right = im.crop((mid_x, mid_y, width, height))

        return top_left, top_right, bottom_left, bottom_right

async def download_image(url, filename, prompt_id):
    """Download an image from a URL and split it into four equal parts."""
    response = requests.get(url)
    #filename = re.findall("\d.*", filename)[0]

    if response.status_code == 200:

        # Define the input and output folder paths
        input_folder = DISCORD.path.input
        output_folder = DISCORD.path.output

        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        # Check if the output folder exists, and create it if necessary
        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(input_folder, exist_ok= True)

        with open(os.path.join(input_file), "wb") as f:
            f.write(response.content)

        logger.info(f"Image downloaded: {filename}")

        output_images = []
        if "UPSCALED_" not in filename:
            file_prefix = os.path.splitext(filename)[0]
            # Split the image
            #top_left, top_right, bottom_left, bottom_right = split_image(input_file)
            images = split_image(input_file)
            # Save the output images with dynamic names in the output folder
            file_names = [f"{file_prefix}_top_left.jpg", f"{file_prefix}_top_right.jpg", f"{file_prefix}_bottom_left.jpg", f"{file_prefix}_bottom_right.jpg"]
            for image, filename in zip(images, file_names):
                output_file = os.path.join(output_folder, filename)
                image.save(output_file)
                #many images saved
                output_images.append((output_file, filename))
        else:
            os.rename(input_file, output_file)
            output_images.append(output_file)
            output_images.append((output_file, filename))
        # Delete the input file
        os.remove(input_file)

        for output_img_path, output_filename in output_images:
            # Uploading them to Cloud Storage
            gcp_img_url = cloud_conn.upload_image(output_img_path, output_filename)
            # Uploading them to PostgreSQL DatBase
            timestamp = datetime.now()
            # Image Upload
            image_data = ImageSchema(
                created_at = timestamp,
                url = gcp_img_url
            )
            image_created = create_image(db=db, image=image_data)
            # Image Prompt Base Upload
            image_prompt_data = ImagePromptBaseSchema(
                image_id = image_created.id,
                prompt_id = prompt_id,
                created_at = timestamp
            )
            create_image_prompt_base(db=db, image_prompt_base=image_prompt_data)
            #cleaning files
            os.remove(output_img_path)

        logger.info(f"Images succesfully uploaded to Cloud Storage & PostgreSQL")


@client.event
async def on_ready():
    """Print a message when the bot is connected."""
    logger.info("Bot connected")

@client.event
async def on_message(message):
    """Download images from messages."""
    for attachment in message.attachments:
        next_unloaded_prompt_id = get_next_unloaded_prompts(db=db).id
        if "Upscaled by" in message.content:
            file_prefix = 'UPSCALED_'
        else:
            file_prefix = ''
        if attachment.filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            await download_image(attachment.url, f"{file_prefix}{attachment.filename}", prompt_id = next_unloaded_prompt_id)

if __name__ == "__main__":
    client.run(cfg.MIDJOURNEY_DOWNLOAD_BOT_TOKEN)