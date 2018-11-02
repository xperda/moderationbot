import discord
import sqlite3

from discord.ext import commands

#util imports
from utils.config import ConfigLoader
from utils.database import DatabaseHandler
from utils.error import CommandErrorHandler


ISCONFIG = ConfigLoader().check_for_bot_config()
if ISCONFIG:
    print("Cannot find config.ini file, please restart the bot with one.")


PREFIX = ConfigLoader().load_config_setting('Bot','command_prefix')
DESC = ConfigLoader().load_config_setting('Bot','description')
TOKEN = ConfigLoader().load_config_setting('Bot','bot_token')


bot = commands.Bot(command_prefix=PREFIX,description=DESC)

bot.remove_command('help')

cogs = ['cogs.basic',
        'cogs.filter',
        'cogs.info',
        'cogs.mod',
        'cogs.moderation']

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')


#main file
if __name__ == '__main__':
    for c in cogs:
        try:
            bot.load_extension(c)
            print(f'{c} loaded')
        except Exception as e:
            print(f'Failed to load extension {c}.')



bot.run(TOKEN)