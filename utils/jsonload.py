import json
import os

class JsonLoader:

    def __init__(self):
        self.jsonfile = "users.json"
        self.jsonstring = "{}"

    def checkJson(self):
        if not os.path.exists(self.jsonfile):
            print("Generating json file..")
            fp = open(self.jsonfile,"w")
            fp.write(self.jsonstring)
            fp.close()
        else:
            print("Found json file..")
            pass
