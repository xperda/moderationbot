import discord
import asyncio

from discord.ext import commands


class basicCog:

    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self,message):
        await self.bot.send_message(message.channel,"Message Deleted")


    @commands.command(name="ping",pass_context=True)
    async def ping(self):
        await self.bot.say("pong")

    @commands.command(name="echo",pass_context=True)
    async def echo(self, *args):
        await self.bot.says(*args)

    @commands.command(name="clear", pass_context=True)
    @commands.bot_has_permissions()
    async def clear(self, ctx, amount=100):
         channel = ctx.message.channel
         messages = []
         async for msg in self.bot.logs_from(channel, limit=int(amount)):
            messages.append(msg)
         await self.bot.delete_messages(messages)
         await asyncio.sleep(1.2)



def setup(bot):
    bot.add_cog(basicCog(bot))
