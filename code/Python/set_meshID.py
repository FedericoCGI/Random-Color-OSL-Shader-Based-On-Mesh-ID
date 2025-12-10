#import set_meshID
#import importlib
#importlib.reload(set_meshID)

import maya.cmds as cmds

def set_meshID():
    
    # get a list of selected objects
    selected_objects: list = cmds.ls(selection=True)

    # set an id mesh for every selected object
    meshID: int = 0

    print(*selected_objects, sep="\n")

    for object in selected_objects:

        shapes: list = []

        '''
        Quando in viewport clicchi un oggetto, selezioni la transform, non la shape.
        Il menu Attributes > V-Ray > User Attributes in realtà lavora sulla shape.
        Quindi, per imitare esattamente quel comportamento via script, il codice fa:
        '''

        shape_node: str = object + "Shape"

        # select object shape node
        cmds.select(shape_node)
        shape_selected = cmds.ls(selection = True)
        print("********", *shape_selected, sep="\n")

        # set attribute:
        node_attribute: str = ".vrayUserAttributes"

        # active attribute on shape node
        if not cmds.attributeQuery("vrayUserAttributes", node=shape_node, exists=True):
            cmds.addAttr(shape_node, ln="vrayUserAttributes", dt="string")
        cmds.setAttr(shape_node + node_attribute, f"meshID={meshID}", type="string" )

        cmds.select(object)
        # active attribute on transform
        if not cmds.attributeQuery("vrayUserAttributes", node=object, exists=True):
            cmds.addAttr(object, ln="vrayUserAttributes", dt="string")
        cmds.setAttr(object + node_attribute, f"meshID={meshID}", type="string" )

        # update meshID
        meshID += 1


set_meshID()
print("Fatto")

