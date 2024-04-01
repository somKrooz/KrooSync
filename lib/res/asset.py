import hou
from .helpers.mtx import MTX
from .helpers.ast import loadAssets
from .helpers.usdAsset import USD
from .helpers.foliage import Foliage

def Ast(json):
    loadAssets(json)

def mtlX(json):
    MTX(json,"/mat")

def USDAsset(json):
   USD(json)

def Folliage(json):
    Foliage(json)



