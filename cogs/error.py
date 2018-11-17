import traceback
import discord

from discord.ext import commands


class ErrorCog:

    def __init__(self, bot):
        self.bot = bot


    async def on_command_error(self, error: Exception,ctx:commands.Context):
        '''
        Override the default on_command error for discord.py
        Modification from https://gist.github.com/Vexs/daa1dcc92ff80fad7ca020d0f7bb4f75

        '''
        if hasattr(ctx.command,'on_error'):
            return

        channel = ctx.message.channel
        ignored = (commands.errors.CommandNotFound, commands.errors.UserInputError)
        if isinstance(error, ignored):
            pass
        elif isinstance(error, commands.errors.NoPrivateMessage):
            await self.bot.send_message(channel,"{} cannot be used in a private message".format(ctx.message.author.mention))
            return
        elif isinstance(error, commands.errors.DisabledCommand):
            await self.bot.send_message(channel,"{} is disabled.".format(ctx.command))
            return
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
             await self.bot.send_message(channel,"I cannot find the member your requested.")
             return
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            formatter = commands.formatter.HelpFormatter()
            await self.bot.send_message(("{} You are missing required arguments.\n{}"
                          .format(ctx.message.author.mention, formatter.format_help_for(ctx, ctx.command)[0])))
            return


def setup(bot):
    bot.add_cog(ErrorCog(bot))