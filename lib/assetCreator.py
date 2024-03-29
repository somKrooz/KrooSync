import hou
from abc import abstractmethod , ABCMeta
from .res import material
from .res import asset

class IMetaData(metaclass=ABCMeta):

    @abstractmethod
    def Generator():
        pass

class Material(IMetaData):
    def __init__(self,json):
        self.name = "material"
        self.json = json
        
    def Generator(self):
       material.mtlX(self.json)

class Asset(IMetaData):
    def __init__(self,json):
        self.name = "Asset"
        self.json = json

    def Generator(self):
        asset.Ast(self.json)

class USD(IMetaData):
    def __init__(self,json):
        self.name = "USD"
        self.json = json

    def Generator(self):
        pass ## add Usd Asset logic 

        
        
        
