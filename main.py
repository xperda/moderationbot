import discord
import sqlite3
from cogs import filter


from discord.ext import commands

bot = commands.Bot(command_prefix="?",description="test")
bot.remove_command('help')

cogs = ['cogs.basic',
        'cogs.filter',
        'cogs.info',
        'cogs.mod',
        'cogs.usrmgmt']

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



bot.run('NTA2MzMyMzc3MTcwMDUxMTAz.DrqscA.hZqpb2KiuB3YSLoiCUhvl_-G3h4')