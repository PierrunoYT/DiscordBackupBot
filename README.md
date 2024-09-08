# Discord Message Backup Bot

This Discord bot allows server administrators to backup messages from channels and manage those backups.

## Features

- Backup messages from a specific channel
- Backup messages from all accessible channels in a server
- List existing backup files
- Delete specific backup files
- Custom help command

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a Discord bot and get its token
4. Update the `config.py` file with your Discord bot token
5. Run the bot:
   ```
   python main.py
   ```

## Commands

- `!backup_channel [channel]`: Backs up messages from a specific channel (or the current channel if not specified)
- `!backup_server`: Backs up messages from all accessible channels in the server
- `!list_backups`: Lists all existing backup files
- `!delete_backup <filename>`: Deletes a specific backup file
- `!help`: Displays information about available commands

## Configuration

You can modify the following settings in `config.py`:

- `DISCORD_TOKEN`: Your Discord bot token
- `COMMAND_PREFIX`: The prefix used for bot commands (default: '!')
- `CHANNEL_MESSAGES_DIR`: Directory for saving channel messages
- `SINGLE_CHANNEL_FILE_FORMAT`: File name format for single channel backups
- `REQUIRED_PERMISSION`: Permission required to use bot commands (default: 'administrator')
- `MESSAGE_HISTORY_LIMIT`: Limit on the number of messages to backup (None for no limit)
- `FILE_ENCODING`: Encoding for file operations (default: 'utf-8')
- `JSON_INDENT`: Indentation for JSON files (default: 4)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
