import discord
import time
from discord.ext import commands

class Info:



    def __init__(self,bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(
            title="Command List",
            color=discord.Colour.red()
        )

        embed.add_field(name="ping", value="ping - Returns a pong")
        embed.add_field(name="echo", value="echo - Echoes what you typed ")
        embed.add_field(name="kick", value="kick - Kick someone from the server")
        embed.add_field(name="ban", value="ban - Ban someone from the server")
        embed.add_field(name="banlist", value='banlist - Shows a list of banned users')

        await self.bot.send_message(ctx.message.channel,embed=embed)

    @commands.command(pass_context=True)
    async def userinfo(self,ctx,user:discord.Member):
        channel = ctx.message.channel
        if user == None:
            user=ctx.author

        profile = discord.Embed
        profile.add_field(name="Created on",value=user.created_at)
        profile.add_field(name="Joined server on", value=user.joined_at)
        profile.add_field(name="Roles",value=user.roles,inline=False)
        profile.set_footer(text="User ID:{}".format(user.id))

        await self.bot.send_message(channel,embed=profile)


def setup(bot):
    bot.add_cog(Info(bot))