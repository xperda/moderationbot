import discord
import os
import datetime

from discord.ext import commands
from utils.database import DatabaseHandler
from datetime import datetime

#queries
getwarn ="SELECT warnings FROM users WHERE discordID = {0}"
replacewarn = "INSERT OR REPLACE INTO users (discordID, warnings) VALUES (?,?) "

class Moderation:
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def warn(self,ctx,user:discord.Member,warning:int,reason):
        addWarnings(user.id,warning)
        if int(getWarnings(user.id)) > 4:
            await self.bot.kick(user)
        else:
            pass



        embed=discord.Embed(title="User has been warned")
        embed.add_field(name="Member", value="{} ".format(user) + "(<@{}>)".format(user.id), inline=False)
        embed.add_field(name="Reason", value = "{} ".format(reason))
        embed.timestamp = datetime.datetime.now()

        await self.bot.send(embed=embed)



def addWarnings(self,user_id):
    points = int(DatabaseHandler().get_result(getwarn.format(user_id)))
    points =1
    DatabaseHandler().insert_into_database(replacewarn,(str(user_id),points))


def deleteWarnings(self,user_id):
    points = int(DatabaseHandler().get_result(getwarn.format(user_id)))
    points-=1
    DatabaseHandler().insert_into_database(replacewarn, (str(user_id), points))


def getWarnings(self,user_id):
    return DatabaseHandler().get_result("SELECT warnings FROM users WHERE discordID = {0}".format(user_id))


def setup(bot):
    bot.add_cog(Moderation(bot))

