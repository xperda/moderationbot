import discord
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


def setup(bot):
    bot.add_cog(Info(bot))