import asyncio

import discord
import datetime
from discord.ext import commands
from discord.ext.commands import CheckFailure
from utils.database import DatabaseHandler


class ModCog:
    def __init__(self,bot):
        self.bot = bot

    def kickbanEmbed(self,msg,user:discord.Member):
        datestamp = datetime.datetime.now().strftime("%d %b %Y ")
        timestamp = datetime.datetime.now().strftime("%H : %M : %S")
        current_time = datestamp+timestamp
        embed = discord.Embed(
            title="Mod Message",
            color=discord.Colour.dark_green()
        )
        embed.add_field(name=msg,value=f"{current_time}")
        embed.set_thumbnail(url=user.avatar_url)
        return embed


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True,kick_members=True)
    async def kick(self ,ctx,user:discord.Member,reason=""):
        if user.id is discord.Server.owner_id:
            await self.bot.say("You can't kick your Overlord!")
            return

        if user.id is ctx.message.author.id:
            await self.bot.say( "You can't kick yourself!" )
            return

        try:
            if reason == "":
                msg = "You have been kicked from the server"
            else:
                msg = "You have been kicked from the server for {}".format("reason")
            msg += "\nYou can rejoin the server, but please read and respect the rules of the server before rejoining."
            await self.bot.send_message(user, msg)
            embed = self.kickbanEmbed( "**{}** has been kicked from the server".format( user.name ), user )
            asyncio.sleep(20)
            await self.bot.kick(user)
            await self.bot.send_message(ctx.message.channel,embed=embed)

        except CheckFailure:
            await self.bot.say("You aren't qualified to use this command")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True, ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason=""):
        if user.id is discord.Server.owner_id:
            await self.bot.say( "You can't ban your Overlord!" )
            return

        if user.id is ctx.message.author.id:
            await self.bot.say( "You can't ban yourself!" )
            return

        try:
            if reason == "":
                    msg = "You have been banned from the server"
            else:
                    msg = "You have been banned from the server for {}".format("reason")
            await self.bot.send_message(user, msg)
            embed = self.kickbanEmbed( "**{}** has been banned from the server".format( user.name ), user )
            asyncio.sleep(20)
            DatabaseHandler().delete_row_db( str( user.id ) )
            await self.bot.ban(user)
            await self.bot.send_message( ctx.message.channel,embed=embed)

        except CheckFailure:
            await self.bot.say("You aren't qualified to use this command")

    @commands.command(pass_context=True)
    async def banlist(self,ctx):
        banendUsers = await self.bot.get_bans(ctx.message.server)
        for user in banendUsers:
            await self.bot.say("{}".format(user.name + " : " + user.id))

def setup(bot):
    bot.add_cog(ModCog(bot))

