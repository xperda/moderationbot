import json
from discord.ext import commands


class Filter:

    with open('banwords.json') as ban:
        banned = json.load(ban)

    def __init__(self,bot):
        self.bot = bot
    #word filter
        @bot.event
        async def on_message(message):
            if any(word in message.content.lower() for word in banned):
                await bot.delete.message(message)
                mention = '{0.author.mention}'.format(message)
                await bot.send_message(message.channel,mention)

def setup(bot):
    bot.add_cog(Filter(bot))