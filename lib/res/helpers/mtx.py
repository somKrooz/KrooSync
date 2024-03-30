import hou

def MTX(json,path):

    name = json[0]["name"]
    MainPath = hou.node(str(path))
    subnet = MainPath.createNode("subnet",name ,force_valid_node_name = True)

    surfaceMTX = subnet.createNode("mtlxstandard_surface")
    dispMtx = subnet.createNode("mtlxdisplacement")
    collect = subnet.createNode("collect")
    surfaceMTX.parm("specular_roughness").set(1)
    dispMtx.parm("scale").set("0.01")

    collect.setInput(0,surfaceMTX)
    collect.setInput(1,dispMtx)

    paths = json[0]["components"]
    for i in paths:
        map = str(i["path"])
        
        if map.__contains__("Albedo"):
            Base_Color = subnet.createNode("mtlxtiledimage","albedo_map")
            colorCorrect = subnet.createNode("mtlxcolorcorrect","ColorCorrect")
            Base_Color.parm('file').set(map)
            colorCorrect.setInput(0,Base_Color)
            surfaceMTX.setInput(1,colorCorrect)     

        if map.__contains__("Roughness"):
            Roughness = subnet.createNode("mtlxtiledimage","roughness_map")
            Roughness.parm("signature").set("Float")
            remap = subnet.createNode("mtlxremap","roughness_remap")
            Roughness.parm('file').set(map)
            remap.setInput(0,Roughness)
            surfaceMTX.setInput(6,remap)

        if map.__contains__("Normal"):
            Normal = subnet.createNode("mtlxtiledimage","normal_map")
            normCon = subnet.createNode("mtlxnormalmap")
            normCon.parm("scale").set("0.3")

            Normal.parm('file').set(map)
            normCon.setInput(0,Normal) 
            surfaceMTX.setInput(40,normCon)     

        if map.__contains__("Opacity"):
            Opcaity = subnet.createNode("mtlxtiledimage","opacity_map")
            Opcaity.parm('file').set(map)
            surfaceMTX.setInput(38,Opcaity) 

        if map.__contains__("Displacement"):
            Displacement = subnet.createNode("mtlxtiledimage","displacement_map")
            Displacement.parm("signature").set("Float")
            Displacement.parm('file').set(map)
            remap = subnet.createNode("mtlxremap","displacement_remap")
            remap.parm('outlow').set(-0.5)
            remap.parm('outhigh').set(0.5)
            remap.setInput(0,Displacement)
            dispMtx.setInput(0,remap)
    collect2 = MainPath.createNode("collect",f"{name}_OUT_" ,force_valid_node_name = True)
    collect2.setInput(0,subnet,subnet.outputIndex('surface'))
    collect2.setInput(1,subnet,subnet.outputIndex('displacement'))
    subnet.layoutChildren()
    MainPath.layoutChildren()