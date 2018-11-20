import discord
import logging
from discord.ext import commands

# util imports
from utils.config import ConfigLoader
from utils.database import DatabaseHandler
from setuptools import setup, find_packages


# Setup logger
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('@%(name)s [%(levelname)s] %(asctime)s: %(message)s'))

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

ISCONFIG = ConfigLoader().check_for_bot_config()
print(ISCONFIG)
if not ISCONFIG:
    print("Cannot find the config.ini file. Restart the bot with ini file")


PREFIX = ConfigLoader().load_config_setting('Bot', 'command_prefix')
DESC = ConfigLoader().load_config_setting('Bot', 'description')
TOKEN = ConfigLoader().load_config_setting('Bot', 'bot_token')
DATABASE = DatabaseHandler().check_db_file()


bot = commands.Bot(command_prefix=PREFIX, description=DESC)
# To remove the default help command
bot.remove_command( 'help' )



cogs = ['cogs.basic',
        'cogs.censor',
        'cogs.error',
        'cogs.info',
        'cogs.mod',
        'cogs.warn']


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id} \nVersion: {discord.__version__}\n')
    await bot.change_presence( game=discord.Game( name='Use ' + PREFIX + 'help for help' ) )




def main():
    for c in cogs:
        try:
            bot.load_extension( c )
            print( f'{c} loaded' )
        except Exception as e:
            print( f'Failed to load extension {c}.' )
    try:
        bot.run( TOKEN )
    except discord.errors.LoginFailure:
        print("\nUnauthorized, please use valid token")
        return

# module needed to run a python file
if __name__ == '__main__':
    main()
