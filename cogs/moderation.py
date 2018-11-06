import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure


class Moderation:
    def __init__(self,bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True,kick_members=True)
    async def kick(self ,user: discord.Member):
        try:
            msg = "{} was kicked from {}".format(user.display_name,self.bot.server.name)
            msg += "\nYou can rejoin the server, but please read and respect the rules of the server before rejoining."
            await self.bot.kick(user)
            await self.bot.send_message(msg)
        except discord.errors.Forbidden:
            self.bot.says("I don't have the permission to do this command")
        except CheckFailure:
            self.bot.says("You aren't qualified to use this command")

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, user: discord.Member):
            try:
                try:
                    member = ctx.message.mentions[0]
                    msg = "You were banned from the {}.".format(self.bot.server.name)
                    self.bot.send_message(member, msg)
                except discord.errors.Forbidden:
                    pass
            except discord.errors.Forbidden:
                self.bot.says("I don't have the permission to do this command")
            await self.bot.ban(user)
            await self.bot.says("{} has been banned.".format(self.bot.escape_name(user)))






def setup(bot):
    bot.add_cog(Moderation(bot))

