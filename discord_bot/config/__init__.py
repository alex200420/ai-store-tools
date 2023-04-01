import os
from brainbite.yaml_classes import YAML_Handler

PATH = 'discord_bot_cfg.yaml' #from settings
YAML_CLASS = YAML_Handler(PATH)

# Load YAML variables
DISCORD = YAML_CLASS.get_yaml_unpacked('discord')

MIDJOURNEY_DOWNLOAD_BOT_TOKEN = os.environ.get("MIDJOURNEY_DOWNLOAD_BOT_TOKEN")