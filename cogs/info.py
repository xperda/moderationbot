import discord
import asyncio
from discord.ext import commands


class InfoCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        commandembed = discord.Embed(title="**__Command List__**", color=discord.Colour.blue())

        commandembed.add_field(name="ping", value="Returns a pong", inline=False)
        commandembed.add_field(name="echo", value="Echoes what you typed ", inline=False)
        commandembed.add_field( name="whois", value="Get a user profile", inline=False)
        commandembed.add_field( name="__Moderator commands__", value="Commands only available to mods", inline=False )
        commandembed.add_field(name="kick", value="Kick someone from the server", inline=True)
        commandembed.add_field(name="ban", value="Ban someone from the server", inline=True)
        commandembed.add_field(name="banlist", value='Shows a list of banned users', inline=True)
        commandembed.add_field( name="warn", value='Adds a warning to the user', inline=True)
        commandembed.add_field( name="unwarn", value='Removes a warning from the user', inline=True )
        commandembed.add_field( name="warning", value='Displays user current warnings', inline=True )
        commandembed.add_field( name="__Chat Filter__", value='Filter than censors profanities and mention spam ', inline=False )
        commandembed.add_field( name="censor", value='Turns chat filter on or off', inline=True )
        commandembed.add_field( name="censorstatus", value='Displays filter current status', inline=True )
        commandembed.add_field( name="blacklist", value='Shows a list of banned words on the server', inline=True )

        await self.bot.send_message(ctx.message.channel, embed=commandembed)


    @commands.command(pass_context=True)
    async def whois(self,ctx,user:discord.Member):

        profile = discord.Embed(title=user.name,color=discord.Colour.blue())
        profile.set_thumbnail(url=user.avatar_url)
        profile.add_field(name="ID",value=user.id,inline=False)
        profile.add_field(name="Date Joined", value=user.joined_at)


        await self.bot.send_message(ctx.message.channel,embed=profile)


def setup(bot):
    bot.add_cog(InfoCog(bot))
