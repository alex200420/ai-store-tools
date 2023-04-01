import os
from brainbite.yaml_classes import YAML_Handler

PATH = 'config.yaml' #from settings
YAML_CLASS = YAML_Handler(PATH)

# Load YAML variables
DISCORD = YAML_CLASS.get_yaml_unpacked('discord')

# Load environment variables
DISCORD_ACCOUNT_TOKEN = os.environ.get("DISCORD_ACCOUNT_TOKEN")
DISCORD_SERVER_ID = os.environ.get("DISCORD_SERVER_ID")
DISCORD_CHANNEL_ID = os.environ.get("DISCORD_CHANNEL_ID")