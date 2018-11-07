import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CheckFailure


class Moderation:
    def __init__(self,bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True,kick_members=True)
    async def kick(self ,ctx,user:discord.Member,reason=""):

        author = ctx.message.author

        try:
            if reason == "":
                msg = "You have been kicked from the server"
            else:
                msg = "You have been kicked from the server for {}".format("reason")
            msg += "\nYou can rejoin the server, but please read and respect the rules of the server before rejoining."
            await self.bot.kick(user)
            await self.bot.send_message(author, msg)
        except discord.errors.Forbidden:
            await self.bot.say("I don't have the permission to do this command")
        except CheckFailure:
            await self.bot.say("You aren't qualified to use this command")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True, ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason=""):

        author = ctx.message.author

        try:
            if reason == "":
                    msg = "You have been banned from the server"
            else:
                    msg = "You have been banned from the server for {}".format("reason")
            await self.bot.ban(user)
            await self.bot.send_message(author, msg)
        except discord.errors.Forbidden:
            await self.bot.say("I don't have the permission to do this command")
        except CheckFailure:
            await self.bot.say("You aren't qualified to use this command")

    @commands.command(name="clear", pass_context=True)
    async def clear(self, ctx, amount):
        channel = ctx.message.channel
        messages = []
        async for msg in self.bot.logs_from(channel, limit=int(amount)):
            messages.append(msg)
        await asyncio.sleep(1)
        await self.bot.delete_messages(messages)


def setup(bot):
    bot.add_cog(Moderation(bot))

