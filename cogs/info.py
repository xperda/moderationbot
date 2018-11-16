import discord
import time
from discord.ext import commands


class InfoCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):

        aboutembed = discord.Embed(color=discord.Colour.blue())
        commandembed = discord.Embed(title="**__Command List__**", color=discord.Colour.blue())
        modembed = discord.Embed(title="**__Mod Commands__**", color=discord.Colour.blue())
        warnembed = discord.Embed( title="**__Warn Commands__**", color=discord.Colour.blue() )
        filterembed = discord.Embed( title="**__Filter Commands__**", color=discord.Colour.blue() )


        greeting = "Hello, I am {}".format(self.bot.user.name)
        desc = "My existence is to assist you in managing your server, I can help you to censor, kick and ban anyone " \
               "you don't like. It doesn't matter if you want to be a rule your server democratically or with an iron " \
               "fist. I am always here to help you in your regime."

        aboutembed.add_field(name=greeting, value=desc)

        commandembed.add_field(name="ping", value="Returns a pong", inline=True)
        commandembed.add_field(name="echo", value="Echoes what you typed ", inline=True)
        modembed.add_field(name="kick", value="Kick someone from the server", inline=True)
        modembed.add_field(name="ban", value="Ban someone from the server", inline=True)
        modembed.add_field(name="banlist", value='Shows a list of banned users', inline=True)
        warnembed.add_field( name="warn", value='Adds a warning to the user', inline=True )
        warnembed.add_field( name="unwarn", value='Removes a warning from the user', inline=True )
        warnembed.add_field( name="warnings", value='Displays user current warnings', inline=True )
        filterembed.add_field( name="filter", value='Turns filter on or off', inline=True )
        filterembed.add_field( name="filterstatus", value='Displays filter current status', inline=True )
        filterembed.add_field( name="blacklist", value='Shows a list of banned words on the server', inline=True )
        await self.bot.send_message(ctx.message.channel, embed=aboutembed)
        await self.bot.send_message(ctx.message.channel, embed=commandembed)
        await self.bot.send_message( ctx.message.channel, embed=modembed)
        await self.bot.send_message( ctx.message.channel, embed=warnembed)
        await self.bot.send_message( ctx.message.channel, embed=filterembed)

    @commands.command(pass_context=True)
    async def whois(self,ctx,user:discord.Member):

        profile = discord.Embed(title=user.name,color=discord.Colour.blue())
        profile.set_thumbnail(url=user.avatar_url)
        profile.add_field(name="ID",value=user.id,inline=False)
        profile.add_field(name="Date Joined", value=user.joined_at)

        await self.bot.send_message(ctx.message.channel,embed=profile)


def setup(bot):
    bot.add_cog(InfoCog(bot))
