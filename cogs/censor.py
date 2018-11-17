import discord
import asyncio
import re

from discord.ext import commands
from utils.database import DatabaseHandler


blacklist = ["FUCK","SHIT","DAMN"]
INVITE = re.compile(r"(?:https?:\/\/)?(?:www\.)?(?:discord\.(?:gg|io|me|li)|discordapp\.com\/invite)\/([\w|\d|-]+)",
    flags=re.IGNORECASE)



class CensorCog:

    def __init__(self, bot):
        self.bot = bot
        self.status = False
        self.mentioned = 0


    async def on_message(self, message):
        if not message.author.server_permissions.administrator:
           await self.track_mention(message)
           await self.censor_message(message)


    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def censor(self, ctx, switched: str):
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
    async def censorstatus(self):
        await self.bot.say("Filter Status : {}".format(self.status))

    @commands.command(pass_context=True)
    async def blacklist(self):
        for x in blacklist:
            msg = x + ", "

        await self.bot.say("**__Blacklist Words__**")
        await self.bot.say("```{}```".format(msg))

    async def censor_message(self,message:discord.Message):

        await self.track_mention(message)

        sentence = message.content.split( " " )
        for word in sentence:
            if word.upper() in blacklist and self.status:
                try:
                    await self.bot.delete_message( message )
                    await self.bot.send_message(message.channel, "You aren't allowed to say that in here!" )
                    return
                except discord.errors.NotFound:
                    pass

    async def track_mention(self,message:discord.Message):
        if "@" in message.content and not self.mentioned >4:
            self.mentioned += 1
        else:
            self.mentioned = 0
            await self.bot.send_message( message.channel, "Stop mention spamming! You have been warned" )
            asyncio.sleep(1)
            await self.bot.purge_from(message.channel,limit=30,check=lambda message: message.author.id)
            await self.warn_user(message.author.id)

            return

    async def warn_user(self,user_id):
        count = DatabaseHandler().get_single_row_db(str(user_id))
        count+=1
        DatabaseHandler().update_db(count,user_id)



def setup(bot):
    bot.add_cog(CensorCog(bot))
