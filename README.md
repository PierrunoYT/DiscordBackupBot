# DiscordBackupBot

DiscordBackupBot is a powerful Discord bot designed to help server administrators efficiently backup and manage channel messages. This project was created by PierrunoYT and is available at [DiscordBackupBot](https://github.com/PierrunoYT/DiscordBackupBot).

## Features

- **Channel Backup**: Archive messages from a specific channel
- **Server-wide Backup**: Backup messages from all accessible channels in a server
- **Backup Management**: List and delete existing backup files
- **Custom Help Command**: Easy-to-use help command for quick reference

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/DiscordBackupBot.git
   cd DiscordBackupBot
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a Discord bot and obtain its token from the [Discord Developer Portal](https://discord.com/developers/applications)
4. Create a `.env` file in the project root and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_token_here
   ```
5. Run the bot:
   ```
   python main.py
   ```

## Commands

- `!backup_channel [channel]`: Archives messages from a specific channel (or the current channel if not specified)
- `!backup_server`: Archives messages from all accessible channels in the server
- `!list_backups`: Lists all existing backup files
- `!delete_backup <filename>`: Deletes a specific backup file
- `!help`: Displays information about available commands

## Configuration

You can modify the bot's behavior by editing the `.env` file. Available settings include:

- `DISCORD_TOKEN`: Your Discord bot token
- `COMMAND_PREFIX`: The prefix used for bot commands (default: '!')
- `CHANNEL_MESSAGES_DIR`: Directory for saving channel messages
- `SINGLE_CHANNEL_FILE_FORMAT`: File name format for single channel backups
- `REQUIRED_PERMISSION`: Permission required to use bot commands (default: 'administrator')
- `MESSAGE_HISTORY_LIMIT`: Limit on the number of messages to backup (0 for no limit)
- `FILE_ENCODING`: Encoding for file operations (default: 'utf-8')
- `JSON_INDENT`: Indentation for JSON files (default: 4)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
