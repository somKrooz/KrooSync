import hou
from .MSimports.mtx import MTX
from .MSimports.ast import loadAssets
from .MSimports.usdAsset import USD
from .MSimports.foliage import Foliage

def Ast(json):
    loadAssets(json)

def mtlX(json):
    MTX(json,"/mat")

def USDAsset(json):
   USD(json)

def Folliage(json):
    Foliage(json)



