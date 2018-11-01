import os
import configparser
import errno

#handler for config

def load_config(file):
    return file

class ConfigLoader:
    def __init__(self,bot=None):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
        self.config = load_config('%s.ini' % (os.path.join(self.path, 'config')), )

        self.parser = configparser.ConfigParser()
        self.bot = bot

        #config example from https://github.com/snoringninja/niftybot-discord/blob/master/resources/config.pyk
        def check_for_bot_config():
            if not self.config:
                print("Generating ini file...")
                parser = configparser.ConfigParser()

                parser.add_section("Bot Settings")
                parser.set('Bot Settings', 'owner_id', 'NOT_SET')
                parser.set('Bot Settings', 'server_id', 'NOT_SET')
                parser.set('Bot Settings', 'bot_token', 'NOT_SET')
                parser.set('Bot Settings', 'game_name', 'NOT_SET')
                parser.set('Bot Settings', 'command_prefix', 'NOT_SET')
                parser.set('Bot Settings', 'description', 'Moderation bot by xperda')
                parser.set('Bot Settings', 'sqlite', 'modbot.db')

                with open('%s.ini'
                          % (os.path.join(self.path,'config')),
                          'x') as configfile:
                            parser.write(configfile)
                return True
            return False





