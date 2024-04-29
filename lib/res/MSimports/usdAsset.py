import hou
from .mtx import MTX

def add_underscores(string):
    return string.replace(' ', '_')

def USD(json):
    name = json[0]["name"]
    lod = json[0]["meshList"][0]["path"]

    meshname = add_underscores(name)

    base = hou.node("/obj")
    subnet = base.createNode("subnet",name,force_valid_node_name = True)
    geo = subnet.createNode("geo")
    file = geo.createNode("file")
    file.parm("file").set(str(lod))


    base = hou.node("/stage")
    sopImp = base.createNode("sopimport")
    sopImp.parm("asreference").set(True)
    sopImp.parm("soppath").set(file.path())
    sopImp.parm("primpath").set(f"/{meshname}/geo")

    matlib = base.createNode("materiallibrary")
    matlib.parm("matnode1").set(f"{meshname}_OUT_") 
    matlib.parm("matpath1").set(f"/{meshname}/Mat/{meshname}_OUT_") 

    MTX(json , str(matlib.path()))

    merge = base.createNode("merge")
    merge.setInput(0,sopImp)
    merge.setInput(1,matlib)

    asignmat = base.createNode("assignmaterial")
    asignmat.parm("primpattern1").set(f"/{meshname}/geo") 
    asignmat.parm("matspecpath1").set(f"/{meshname}/Mat/{meshname}_OUT_") 

    asignmat.setInput(0,merge)
    null = base.createNode("null") ##Assign
    null.setInput(0,asignmat)

    null.setDisplayFlag(True)

    geo.layoutChildren()
    base.layoutChildren()


