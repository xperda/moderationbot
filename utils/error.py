from discord.ext import commands

#To handle exceptions from invoking commands
class CommandErrorHandler:
    def __init__(self,bot):
        self.bot = bot

    #THis event is triggered when an exception is raised when invoking a command
    async def on_command_error(self,ctx,error):

        humanerror = (commands.CommandNotFound,commands.UserInputError)
        '''
            
        '''
        if isinstance(error,humanerror):
            return await ctx.send(f'{ctx.command} does not exist.')
        elif isinstance(error,commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} is disabled.')
        elif isinstance(error,commands.BadArgument):
            return await ctx.send('I am sorry, I cannot find this user.')