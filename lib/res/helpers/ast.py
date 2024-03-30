import hou
from .mtx import MTX

def loadAssets(json):
    name = json[0]["name"]
    lod = json[0]["meshList"][0]["path"]
    base = hou.node("/obj")
    subnet = base.createNode("subnet",name,force_valid_node_name = True)
    geo = subnet.createNode("geo")
    matnet = subnet.createNode("matnet")
    MTX(json ,str(matnet.path()))

    file = geo.createNode("file")
    file.parm("file").set(str(lod))
    mtl = geo.createNode("material")
    mtl.parm("shop_materialpath1").set(f"{str(matnet.path())}/{name}_OUT_")

    mtl.setInput(0,file)
    mtl.setRenderFlag(True)
    mtl.setDisplayFlag(True)

    subnet.layoutChildren()
    geo.layoutChildren()

