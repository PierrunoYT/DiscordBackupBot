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

    @commands.command(name='save_channel')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def save_channel(self, ctx, channel: discord.TextChannel = None):
        print("save_channel command called")  # Debug print
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

    @commands.command(name='save_all_channels')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def save_all_channels(self, ctx):
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

    @commands.command(name='list_messages')
    @commands.has_permissions(**{REQUIRED_PERMISSION: True})
    async def list_messages(self, ctx):
        message = "Saved message files:\n"
        
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

# This file is now a cog and will be imported by main.py
