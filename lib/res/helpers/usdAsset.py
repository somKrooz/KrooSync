import hou
from .mtx import MTX


def USD(json):
    name = json[0]["name"]
    lod = json[0]["meshList"][0]["path"]
    base = hou.node("/obj")
    subnet = base.createNode("subnet",name,force_valid_node_name = True)
    geo = subnet.createNode("geo")
    file = geo.createNode("file")
    file.parm("file").set(str(lod))


    base = hou.node("/stage")
    sopImp = base.createNode("sopimport")
    sopImp.parm("soppath").set(file.path())
    sopImp.parm("primpath").set(f"/{name}/geo")

    matlib = base.createNode("materiallibrary")
    matlib.parm("matnode1").set(f"/{name}") # what is this
    matlib.parm("matpath1").set(f"/{name}/mat") # Put it under that

    MTX(json , str(matlib.path()))

    merge = base.createNode("merge")
    merge.setInput(0,sopImp)
    merge.setInput(1,matlib)

    asignmat = base.createNode("assignmaterial")
    asignmat.parm("primpattern1").set(f"/{name}/geo") #Geo Path At Solaris Level
    asignmat.parm("matspecpath1").set(f"/{name}/mat") #Mat path At Solaris Level

    asignmat.setInput(0,merge)
    null = base.createNode("null") ##Assign
    null.setInput(0,asignmat)

    geo.layoutChildren()
    base.layoutChildren()


