import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', 'YOUR_DISCORD_TOKEN_HERE')

# Bot command prefix (used for backup_channel, backup_server, list_backups, delete_backup)
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')

# Directory for saving channel messages
CHANNEL_MESSAGES_DIR = os.getenv('CHANNEL_MESSAGES_DIR', 'channel_messages')

# File name for single channel messages
SINGLE_CHANNEL_FILE_FORMAT = os.getenv('SINGLE_CHANNEL_FILE_FORMAT', '{channel_name}_messages.json')

# Permissions
REQUIRED_PERMISSION = os.getenv('REQUIRED_PERMISSION', 'administrator')

# Message history limit (None for no limit)
MESSAGE_HISTORY_LIMIT = int(os.getenv('MESSAGE_HISTORY_LIMIT', '0')) or None

# Encoding for file operations
FILE_ENCODING = os.getenv('FILE_ENCODING', 'utf-8')

# JSON indentation for saved files
JSON_INDENT = int(os.getenv('JSON_INDENT', '4'))
