import discord
import logging
import traceback

from discord.ext import commands

# util imports
from utils.config import ConfigLoader
from utils.database import DatabaseHandler

ISCONFIG = ConfigLoader().check_for_bot_config()
if ISCONFIG:
    print("Cannot find config.ini file, please restart the bot with one.")

PREFIX = ConfigLoader().load_config_setting('Bot', 'command_prefix')
DESC = ConfigLoader().load_config_setting('Bot', 'description')
TOKEN = ConfigLoader().load_config_setting('Bot', 'bot_token')
DATABASE = DatabaseHandler().check_db_file()


bot = commands.Bot(command_prefix=PREFIX, description=DESC)
# To remove the default help command
bot.remove_command( 'help' )


# Setup logger
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('@%(name)s [%(levelname)s] %(asctime)s: %(message)s'))
logger.addHandler(handler)


cogs = ['cogs.basic',
        'cogs.censor',
        'cogs.error',
        'cogs.info',
        'cogs.mod',
        'cogs.warning']


@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

@bot.event
async def on_message_delete():
    pass


def main():
    for c in cogs:
        try:
            bot.load_extension( c )
            print( f'{c} loaded' )
        except Exception as e:
            print( f'Failed to load extension {c}.' )

    bot.run( TOKEN )

# module needed to run a python file
if __name__ == '__main__':
    main()