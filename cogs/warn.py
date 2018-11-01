from discord.ext import commands

class Warn:
    def __init__(self,bot):
        self.bot = bot





def setup(bot):
    bot.add_cog(Warn(bot))