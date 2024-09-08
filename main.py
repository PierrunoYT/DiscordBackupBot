import discord
from discord.ext import commands
from config import DISCORD_TOKEN, COMMAND_PREFIX
from save_discord_messages import MessageSaver

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Connected to {len(bot.guilds)} guilds:')
    for guild in bot.guilds:
        print(f'- {guild.name} (id: {guild.id})')

# Add the MessageSaver cog
async def setup(bot):
    await bot.add_cog(MessageSaver(bot))

# Run the bot
if __name__ == '__main__':
    bot.loop.run_until_complete(setup(bot))
    bot.run(DISCORD_TOKEN)