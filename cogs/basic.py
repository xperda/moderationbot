import discord
import time

from discord.ext import commands


class basicCog:

    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self,message):
        await self.bot.send_message(message.channel,"Message Deleted")


    @commands.command(name="ping",pass_context=True)
    async def ping(self,ctx):
        initial_time = time.monotonic()
        await self.bot.send_message(ctx.message.channel, 'Pong!')
        pong = '%.2f' % (100*(time.monotonic()-initial_time))
        embed = discord.Embed(color=discord.Colour(0x3498db))
        embed.add_field(name="Modbot Ping",value="Ping - {} ms".format(pong))
        await self.bot.say(embed=embed)
        await self.bot.say(pong)
    @commands.command(name="echo",pass_context=True)
    async def echo(self, *args):
        await self.bot.says(*args)




def setup(bot):
    bot.add_cog(basicCog(bot))
