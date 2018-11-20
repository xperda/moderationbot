import os
import configparser
import errno

#handler for config

class ConfigLoader:
    def __init__(self):
        self.config = "config.ini"
        self.parser = configparser.ConfigParser()

    #config from https://github.com/snoringninja/niftybot-discord/blob/master/resources/config.pyk
    def check_for_bot_config(self):
        if not os.path.exists(self.config):
            print("Generating ini file...")
            parser = configparser.ConfigParser()

            parser.add_section("Bot")
            parser.add_section( "Channel" )
            parser.set('Bot', 'owner_id', '')
            parser.set('Bot', 'server_id', '')
            parser.set('Bot', 'bot_token', '')
            parser.set('Bot', 'command_prefix', '!')
            parser.set('Bot', 'description', 'Moderation bot by xperda')
            parser.set( 'Channel', 'general_id', '' )
            parser.set( 'Channel', 'logging_id', '' )
            with open(self.config,'w') as configfile:
                parser.write(configfile)
                print("Generated config.ini")
            return True
        return False

    def load_config_setting(self, section,var):
        """Load a config setting from the ini."""
        self.parser.read(self.config)
        return self.parser.get(section,var)

    def edit_config(self,section,var,var2):
        self.parser.set(section,var,var2)
        with open('config.ini','wb') as configfile:
            self.parser.write(configfile)





