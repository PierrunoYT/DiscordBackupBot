import json
import discord
from discord.ext import commands
import os

class MessageSaver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='save_channel')
    @commands.has_permissions(administrator=True)
    async def save_channel(self, ctx, channel: discord.TextChannel = None):
        print("save_channel command called")  # Debug print
        if channel is None:
            channel = ctx.channel
        
        messages = []
        async for message in channel.history(limit=None):
            messages.append({
                'author': str(message.author),
                'content': message.content,
                'timestamp': str(message.created_at),
                'attachments': [att.url for att in message.attachments]
            })
        
        filename = f'{channel.name}_messages.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)
        
        await ctx.send(f'Saved {len(messages)} messages from #{channel.name} to {filename}')

    @commands.command(name='save_all_channels')
    @commands.has_permissions(administrator=True)
    async def save_all_channels(self, ctx):
        if not os.path.exists('channel_messages'):
            os.makedirs('channel_messages')

        for channel in ctx.guild.text_channels:
            try:
                messages = []
                async for message in channel.history(limit=None):
                    messages.append({
                        'author': str(message.author),
                        'content': message.content,
                        'timestamp': str(message.created_at),
                        'attachments': [att.url for att in message.attachments]
                    })
                
                filename = f'channel_messages/{channel.name}_messages.json'
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(messages, f, ensure_ascii=False, indent=4)
                
                await ctx.send(f'Saved {len(messages)} messages from #{channel.name} to {filename}')
            except discord.errors.Forbidden:
                await ctx.send(f'Unable to access messages in #{channel.name}. Skipping...')
            except Exception as e:
                await ctx.send(f'An error occurred while saving messages from #{channel.name}: {str(e)}')

        await ctx.send('Finished saving messages from all accessible channels.')

    @commands.command(name='list_messages')
    @commands.has_permissions(administrator=True)
    async def list_messages(self, ctx):
        message = "Saved message files:\n"
        
        if os.path.exists('discord_messages.json'):
            message += "- discord_messages.json\n"
        else:
            message += "- discord_messages.json (not found)\n"
        
        if os.path.exists('channel_messages'):
            for filename in os.listdir('channel_messages'):
                if filename.endswith('.json'):
                    message += f"- channel_messages/{filename}\n"
        else:
            message += "- No channel_messages directory found\n"
        
        if message == "Saved message files:\n":
            message = "No saved message files found."
        
        await ctx.send(message)

# This file is now a cog and will be imported by main.py
