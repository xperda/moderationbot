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

    def loadJson(self,path):
        with open(path,"r") as items:
            return json.load(items)

    def dumpJson(self,path,data):
        with open(path, "w") as items:
           json.dump(data,items)