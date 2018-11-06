import discord
import time
from discord.ext import commands

class Info:



    def __init__(self,bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(
            color=discord.Colour.red()
        )

        embed.add_field(name="help", value="ping - returns a pong")

        await self.bot.send_message(ctx.message.channel,embed=embed)

    @commands.command(pass_context=True)
    async def userinfo(self,ctx,user:discord.Member):
        if user == None:
            user=ctx.author

        profile = discord.Embed
        profile.add_field(name="Created on",value=user.created_at)
        profile.add_field(name="Joined server on", value=user.joined_at)
        profile.add_field(name="Roles",value=user.roles,inline=False)
        profile.set_footer(text="User ID:{}".format(user.id))

        await self.bot.say(embed=profile)


def setup(bot):
    bot.add_cog(Info(bot))