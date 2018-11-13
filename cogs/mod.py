import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CheckFailure



class ModCog:
    def __init__(self,bot):
        self.bot = bot



    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True,kick_members=True)
    async def kick(self ,ctx,user:discord.Member,reason=""):

        try:
            if reason == "":
                msg = "You have been kicked from the server"
            else:
                msg = "You have been kicked from the server for {}".format("reason")
            msg += "\nYou can rejoin the server, but please read and respect the rules of the server before rejoining."
            await self.bot.send_message(user, msg)
            await self.bot.kick(user)
            await self.bot.say("{} has been kicked from the server".format(user.name))

        except CheckFailure:
            await self.bot.say("You aren't qualified to use this command")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True, ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason=""):


        try:
            if reason == "":
                    msg = "You have been banned from the server"
            else:
                    msg = "You have been banned from the server for {}".format("reason")
            await self.bot.send_message(user, msg)
            await self.bot.ban(user)
            await self.bot.say("{} has been banned from the server".format(user.name))

        except CheckFailure:
            await self.bot.say("You aren't qualified to use this command")


    @commands.command(pass_context=True)
    async def banlist(self,ctx):
        banendUsers = await self.bot.get_bans(ctx.message.server)
        for user in banendUsers:
            await self.bot.say("{}".format(user.name + " : " + user.id))





def setup(bot):
    bot.add_cog(ModCog(bot))

