import hou
from abc import abstractmethod , ABCMeta
from .res.asset import mtlX ,Ast ,USDAsset ,Foliage

class IMetaData(metaclass=ABCMeta):
    @abstractmethod
    def Generator():
        pass

class Material(IMetaData):
    def __init__(self,json):
        self.name = "material"
        self.json = json
        
    def Generator(self):
       mtlX(self.json)

class Asset(IMetaData):
    def __init__(self,json):
        self.name = "Asset"
        self.json = json

    def Generator(self):
        Ast(self.json)

class USD(IMetaData):
    def __init__(self,json):
        self.name = "USD"
        self.json = json

    def Generator(self):
        USDAsset(self.json)

class Plants(IMetaData):
    def __init__(self,json):
        self.name = "Foliage"
        self.json = json
    
    def Generator(self):
        Foliage(self.json)

        
        
        
