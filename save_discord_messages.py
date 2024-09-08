import json
import discord
from discord.ext import commands
import os
from config import (
    COMMAND_PREFIX, CHANNEL_MESSAGES_DIR, SINGLE_CHANNEL_FILE_FORMAT,
    REQUIRED_PERMISSION, MESSAGE_HISTORY_LIMIT, FILE_ENCODING, JSON_INDENT
)

class MessageSaver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='backup_channel')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def backup_channel(self, ctx, channel: discord.TextChannel = None):
        print("backup_channel command called")  # Debug print
        if channel is None:
            channel = ctx.channel
        
        messages = []
        async for message in channel.history(limit=MESSAGE_HISTORY_LIMIT):
            messages.append({
                'author': str(message.author),
                'content': message.content,
                'timestamp': str(message.created_at),
                'attachments': [att.url for att in message.attachments]
            })
        
        filename = SINGLE_CHANNEL_FILE_FORMAT.format(channel_name=channel.name)
        with open(filename, 'w', encoding=FILE_ENCODING) as f:
            json.dump(messages, f, ensure_ascii=False, indent=JSON_INDENT)
        
        await ctx.send(f'Saved {len(messages)} messages from #{channel.name} to {filename}')

    @commands.command(name='backup_server')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def backup_server(self, ctx):
        if not os.path.exists(CHANNEL_MESSAGES_DIR):
            os.makedirs(CHANNEL_MESSAGES_DIR)

        for channel in ctx.guild.text_channels:
            try:
                messages = []
                async for message in channel.history(limit=MESSAGE_HISTORY_LIMIT):
                    messages.append({
                        'author': str(message.author),
                        'content': message.content,
                        'timestamp': str(message.created_at),
                        'attachments': [att.url for att in message.attachments]
                    })
                
                filename = os.path.join(CHANNEL_MESSAGES_DIR, SINGLE_CHANNEL_FILE_FORMAT.format(channel_name=channel.name))
                with open(filename, 'w', encoding=FILE_ENCODING) as f:
                    json.dump(messages, f, ensure_ascii=False, indent=JSON_INDENT)
                
                await ctx.send(f'Saved {len(messages)} messages from #{channel.name} to {filename}')
            except discord.errors.Forbidden:
                await ctx.send(f'Unable to access messages in #{channel.name}. Skipping...')
            except Exception as e:
                await ctx.send(f'An error occurred while saving messages from #{channel.name}: {str(e)}')

        await ctx.send('Finished saving messages from all accessible channels.')

    @commands.command(name='list_backups')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def list_backups(self, ctx):
        message = "Backup files:\n"
        
        if os.path.exists('discord_messages.json'):
            message += "- discord_messages.json\n"
        else:
            message += "- discord_messages.json (not found)\n"
        
        if os.path.exists(CHANNEL_MESSAGES_DIR):
            for filename in os.listdir(CHANNEL_MESSAGES_DIR):
                if filename.endswith('.json'):
                    message += f"- {os.path.join(CHANNEL_MESSAGES_DIR, filename)}\n"
        else:
            message += f"- No {CHANNEL_MESSAGES_DIR} directory found\n"
        
        if message == "Saved message files:\n":
            message = "No saved message files found."
        
        await ctx.send(message)

    @commands.command(name='delete_backup')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def delete_backup(self, ctx, filename: str):
        if not filename.endswith('.json'):
            filename += '.json'
        
        file_path = os.path.join(CHANNEL_MESSAGES_DIR, filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
            await ctx.send(f'Backup file {filename} has been deleted.')
        else:
            await ctx.send(f'Backup file {filename} not found.')

    @commands.command(name='help')
    async def help_command(self, ctx):
        help_text = """
        **Available Commands:**
        
        `!backup_channel [channel]`: Backs up messages from a specific channel (or the current channel if not specified).
        `!backup_server`: Backs up messages from all accessible channels in the server.
        `!list_backups`: Lists all existing backup files.
        `!delete_backup <filename>`: Deletes a specific backup file.
        
        Note: All commands require administrator permissions.
        """
        await ctx.send(help_text)

# This file is now a cog and will be imported by main.py
