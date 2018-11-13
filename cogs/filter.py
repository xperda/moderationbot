import discord
import re

from discord.ext import commands
from utils.jsonload import JsonLoader

blacklist = ["FUCK","SHIT","DAMN"]


class FilterCog:

    def __init__(self, bot):
        self.bot = bot
        self.status = False

    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def filter(self, ctx, switched: str):
        if switched == "on":
            if not self.status:
                self.status = True
                await self.bot.say("The filter has been enabled")
            else:
                await self.bot.say("The filter is already enabled!")
                return
        elif switched == "off":
            if self.status:
                self.status = False
                await self.bot.say("The filter has been disabled")
            else:
                await self.bot.say("The filter is already disabled!")
                return
        elif switched == " ":
            await self.bot.say("Don't leave it a blank, please input on or off")
        else:
            await self.bot.say("I have no idea what you want me to do {}.")

    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def filterstatus(self):
        await self.bot.say("Filter Status : {}".format(self.status))

    @commands.command(pass_context=True)
    async def blacklist(self):
        for x in blacklist:
            msg = x + ", "

        await self.bot.say("**__Blacklist Words__**")
        await self.bot.say("```{}```".format(msg))

    # main filters
    async def on_message(self, message):
        sentence = message.content.split(" ")
        print(str(self.status))
        for word in sentence:
            if word.upper() in blacklist and self.status:
                try:
                    await self.bot.purge_message(message)
                    await self.bot.send_message("You aren't allowed to say that in here!")
                except discord.errors.NotFound:
                    return


def setup(bot):
    bot.add_cog(FilterCog(bot))
