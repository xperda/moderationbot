import discord
import asyncio
import traceback

from discord.ext import commands

# util imports
from utils.config import ConfigLoader
from utils.jsonload import JsonLoader

ISCONFIG = ConfigLoader().check_for_bot_config()
if ISCONFIG:
    print("Cannot find config.ini file, please restart the bot with one.")

PREFIX = ConfigLoader().load_config_setting('Bot', 'command_prefix')
DESC = ConfigLoader().load_config_setting('Bot', 'description')
TOKEN = ConfigLoader().load_config_setting('Bot', 'bot_token')
JSON = JsonLoader().checkJson()


bot = commands.Bot(command_prefix=PREFIX, description=DESC)
#To remove the default help command
bot.remove_command('help')



cogs = ['cogs.basic',
        'cogs.filter',
        'cogs.info',
        'cogs.mod',
        'cogs.warning']


@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

'''
@bot.event
async def on_command_error(ctx, error):

    humanerror = (commands.errors.CommandNotFound, commands.errors.UserInputError)
    if isinstance(error, humanerror):
        pass
    elif isinstance(error, commands.errors.CheckFailure):
        await bot.say("{} is not allowed to use this command".format(ctx.message.author.mention))
    elif isinstance(error, commands.errors.DisabledCommand):
        await bot.say("{} is disabled.".format(ctx.command))
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        formatter = commands.formatter.HelpFormatter()
        await bot.say("{} You are missing required arguments.\n{}"
                      .format(ctx.message.author.mention, formatter.format_help_for(ctx, ctx.command)[0]))
'''


# module needed to run a python file
if __name__ == '__main__':
    for c in cogs:
        try:
            bot.load_extension(c)
            print(f'{c} loaded')
        except Exception as e:
            print(f'Failed to load extension {c}.')

bot.run(TOKEN)
