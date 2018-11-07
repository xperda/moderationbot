import json
import os

class JsonLoader:

    def __init__(self):
        pass

    def loadJson(self,path):
        with open(path,"r") as items:
            return json.load(items)

    def dumpJson(self,path,data):
        with open(path, "w") as items:
           json.dump(data,items)