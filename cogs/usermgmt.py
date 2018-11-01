from discord.ext import commands

class Ban:
    def __init__(self,bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Ban(bot))