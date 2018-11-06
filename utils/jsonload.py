import json

class JsonLoader:

    def __init__(self):
        pass

    def loadJson(self,path):
        with open(path) as items:
            return json.load(items)

    def dumpJson(self,path):
        with open(path) as items:
           json.dump(path,items)