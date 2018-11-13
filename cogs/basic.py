import discord
import time

from discord.ext import commands


class BasicCog:

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

    @commands.command(name="echo",pass_context=True)
    async def echo(self, ctx, *args):
        await self.bot.send_message(ctx.message.channel,*args)

    @commands.command(name="clear", pass_context=True)
    async def clear(self, ctx, amount):
        channel = ctx.message.channel
        messages = []
        async for msg in self.bot.logs_from(channel, limit=int(amount)):
            messages.append(msg)
        await self.bot.delete_messages(messages)


def setup(bot):
    bot.add_cog(BasicCog(bot))
