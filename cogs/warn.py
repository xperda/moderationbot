import discord
import json

from discord.ext import commands
from utils.database import DatabaseHandler

class WarningCog:

    def __init__(self, bot):
        self.bot = bot
        self.database = DatabaseHandler()

    async def addWarnings(self, count, user_id):
        count += 1
        self.database.update_db( count, user_id )

    async def deleteWarnings(self, count, user_id):
        if count < 0:
            pass
        else:
            count -= 1
            self.database.update_db( count, user_id )

    @commands.command(name="warning",pass_context=True)
    async def warning(self, ctx, member: discord.Member):
        if member is None:
            pass

        count = self.database.get_single_row_db(str(member.id))
        warnembed = discord.Embed(color=discord.Colour.red())
        warnembed.add_field(name="Current warnings ", value=count)
        warnembed.set_thumbnail(url=member.avatar_url)

        await self.bot.send_message(ctx.message.channel, embed=warnembed)

    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def warn(self, ctx, member: discord.Member):
        if member.id is discord.Server.owner_id:
            await self.bot.say("You can't warn your Overlord!")
            return

        if member.id is ctx.message.author.id:
            await self.bot.say( "You can't warn yourself!" )
            return

        count = self.database.get_single_row_db(str(member.id))
        await self.addWarnings( count, member.id )
        if count <= 3 :
            await self.bot.send_message( ctx.message.channel,
                                         "{} has been __warned__. Your current warnings are {}".format(member.mention,count+1))

        elif count == 4:
            await self.bot.send_message(ctx.message.channel,"{} has been kicked for too many warnings".format(member.name))
            await self.bot.send_message(member,"You have been kicked from the server, get another warning and you will be banned!")
            await self.bot.kick(member)
        else:
            await self.bot.send_message( ctx.message.channel,
                                         "No more chances, {} has been banned".format( member.name ) )
            await self.bot.send_message( member, "You have been banned from the server for being a nuisance." )
            self.database.delete_row_db( str( member.id ) )
            await self.bot.ban( member )


    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def unwarn(self, ctx, member: discord.Member):
        if member.id is discord.Server.owner_id:
            await self.bot.say( "You can't do that to your Overlord!" )
            return

        if member.id is ctx.message.author.id:
            await self.bot.say( "You can't unwarn yourself!" )
            return

        count = self.database.get_single_row_db(str(member.id))

        if count <= 0 :
           await self.bot.send_message(ctx.message.channel,"{} has no warnings.".format(
                                             member.mention))
        else:
            count -= 1
            await self.bot.send_message( ctx.message.channel,
                                         "{} has been __pardoned__. Your current warnings are {}".format(
                                             member.mention, count) )
            await self.deleteWarnings(count,member.id)


    async def on_member_join(self,member):
        channel = member.server.default_channel
        if self.checkID(member.id):
            query = 'INSERT INTO users (id,username,warnings) VALUES (?,?,?)'
            self.database.insert_into_db( query, (str( member.id ), str( member.name ), 0) )
            await self.bot.send_message(channel,"{} has joined the server".format(member.name))

    async def on_member_remove(self,member):
        channel = member.server.default_channel

        await self.bot.send_message(channel,"{} has left the server".format(member.name))

    def checkID(self,id):
        user = self.database.get_all_rows_db()
        if id not in user:
            return True
        else:
            return False

    '''
       @commands.command( name="register", pass_context=True )
       async def register(self, member: discord.Member):
           user_id = DatabaseHandler().get_all_rows_db()
           if member.id == user_id:
               query = 'INSERT INTO users (id,username,warnings) VALUES (?,?,?)'
               self.database.insert_into_db( query, (str( member.id ), str( member.name ), 0) )
               self.bot.say("{} has been registered.".format(member.name))
           else:
               self.bot.say( "I can't register this member, {}.".format( member.name ))
       '''



def setup(bot):
    bot.add_cog(WarningCog(bot))
