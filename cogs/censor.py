import discord
import asyncio
import datetime

from discord.ext import commands
from utils.database import DatabaseHandler

profanities = ['FUCK','ASS','BITCH','CUNT','SHIT','FCUK','FAGGOT','MOTHERFUCKER']


class CensorCog:

    def __init__(self, bot):
        self.bot = bot
        self.status = False
        self.mentioned = 0

    async def on_message(self, message):
        if message.author.server_permissions.administrator :
            return
        if self.status:
           await self.censor_profanity(message)


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
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
        else:
            await self.bot.say("I have no idea what you want me to do. Please input on of off")


    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def censorstatus(self):
        await self.bot.say("Filter Status : {}".format(self.status))

    @commands.command(pass_context=True)
    async def blacklist(self):

        list = [word.lower() for word in profanities]

        await self.bot.say("**__Blacklist Words__**")
        await self.bot.say("```{}```".format(list))

    async def censor_profanity(self,message:discord.Message):

        await self.track_mention( message )
        sentence = message.content.split( " " )
        embed = discord.Embed(
            title="Message Censored",
            color=discord.Colour.red()
        )
        for word in sentence:
            if word.upper() in profanities:
                try:
                    #await self.bot.wait_for_message(author=message.author)
                    await self.bot.delete_message(message)
                    embed.add_field( name=message.author, value=f"```{word.lower()}```", inline=False )
                    await self.bot.send_message( message.channel, embed=embed)
                    return
                except discord.errors.NotFound:
                    pass

    async def track_mention(self,message:discord.Message):
        if "@" in message.content :
            if not self.mentioned >=4:
                self.mentioned += 1
                print(self.mentioned)
            else:
                asyncio.sleep(1)
                await self.bot.purge_from( message.channel, limit=5, check=lambda message: message.author.id )
                asyncio.sleep(1)
                await self.bot.send_message( message.channel, f"Stop spamming, {message.mentions}!" )
                self.mentioned = 0
                return
        else:
            pass

    '''
    async def warn_user(self,user:discord.Member):
        user_id = user.id
        count = DatabaseHandler().get_single_row_db(str(user_id))
        count+=1
        if count < 4:
            return 0
        if count is 4:
            asyncio.sleep(5)
            await self.bot.send_message(user,"You have been kicked from the server for spamming")
            await self.bot.kick(user)
            return 1
        if count >5:
            await self.bot.send_message( user, "You have been banned from the server for excessive spamming" )
            await self.bot.ban(user)
            return 2


        DatabaseHandler().update_db(count,user_id)
    '''
    def kickbanEmbed(self, msg, user: discord.Member):
        datestamp = datetime.datetime.now().strftime( "%d %b &Y " )
        timestamp = datetime.datetime.now().strftime( "%H : %M : %S" )
        current_time = datestamp + timestamp
        embed = discord.Embed(
            title="Mod Message",
            color=discord.Colour.dark_green()
        )
        embed.add_field( name=msg, value=f"{current_time}" )
        embed.set_thumbnail( url=user.avatar_url )
        return embed


def setup(bot):
    bot.add_cog(CensorCog(bot))
