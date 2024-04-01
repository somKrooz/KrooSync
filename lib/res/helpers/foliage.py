import hou
from .mtx import MTX

def add_underscores(string):
    return string.replace(' ', '_')

def Foliage(json):
    asset_name = json[0]["name"]
    name = add_underscores(asset_name)
    base = hou.node("/obj")
    subnet = base.createNode("subnet",asset_name,force_valid_node_name = True)
    geo = subnet.createNode("geo","Varients")
    matnet = subnet.createNode("matnet")
    MTX(json , str(matnet.path()))


    paths = []
    for i in json[0]["lodList"]:
        if i['lod'] == "lod0":
            paths.append(i["path"])
    
    Switch = geo.createNode("switch")
    null = geo.createNode("null")

    id = 0
    for i in paths:
        file = geo.createNode("file")
        file.parm("file").set(str(i))
        mtl = geo.createNode("material")
        mtl.parm("shop_materialpath1").set(f"{str(matnet.path())}/{name}_OUT_")
        mtl.setInput(0,file)

        Switch.setInput(id,mtl)
        id+=1

    null.setInput(0,Switch)
    null.setRenderFlag(True)
    null.setDisplayFlag(True)

    geo.layoutChildren()
    subnet.layoutChildren()