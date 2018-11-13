import discord
import json

from discord.ext import commands

filepath = 'users.json'


class WarningCog:

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.has_permissions()
    async def register(self, ctx, user: discord.Member):
        warnings = loadJson(filepath)

        if user.id not in warnings:
            json_string = {user.id:{"name": user.name, "warnings": 0}}
            appendJson(filepath,json_string)
            await self.bot.send_message(ctx.message.channel, "{} has been registered.".format(user.name))
        elif user.id in warnings:
            await self.bot.send_message(ctx.message.channel, "{} is already registered.".format(user.name))
        else:
            await self.bot.send_message(ctx.message.channel, "I am unable to register this user")

    async def on_member_join(self,member:discord.Member):
        json_string = {member.id: {"name": member.name, "warnings": 0}}
        appendJson(filepath, json_string)
        await self.bot.say("{} has joined {}".format(member.name,self.bot.user.server))


    async def on_member_leave(self, member:discord.Member):
        delJson(filepath, member.id)
        await self.bot.say("{} has left {}".format(member.name, self.bot.user.server))

def loadJson(path):
    with open(path,"r") as items:
            return json.load(items)

def appendJson(path,data):
    with open(path, "w") as items:
        json.dump(data,items,indent=3)

def delJson(path,_id_):
    data = loadJson(path)
    if _id_ in data:
        del data[_id_]

    with open(path, "w") as items:
        json.dump(data,indent=2)

def setup(bot):
    bot.add_cog(WarningCog(bot))
