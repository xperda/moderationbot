import discord
import os
import datetime

from discord.ext import commands
from datetime import datetime

class Moderation:
    def __init__(self,bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Moderation(bot))