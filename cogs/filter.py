import json
from discord.ext import commands



class Filter:

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def banwordlist(ctx):
        for x in chat_filter:
         ctx.sendMessage(x)

def check_banwordlist(word):
    if word in chat_filter:
        return True
    else:
        return False

def deleteMessage():
    for word in filter.check_banwordlist()
        if word.upper() in chat_filter:



def setup(bot):
    bot.add_cog(Filter(bot))
