"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""


__author__ = "IlmoK"
__version__ = "2023.12.14"

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghc


CollisionIndices = []
ListLens = []

for i in range(len(mesh_faces)):
    
    CollisionList = ghc.ReplaceItems(mesh_faces, 0, i, True)
    print CollisionList
    face = mesh_faces[i]
    isColliding = True
    count = 0
    
    while isColliding==True:
        
        CollisionData = ghc.CollisionOneXMany(face, CollisionList)
        isColliding = CollisionData[0]
        CollisionIndex  = CollisionData[1]
        
        if CollisionIndex!= -1:
            
            CollisionIndices.append(CollisionIndex)
            CollisionList = ghc.ReplaceItems( CollisionList, 0, CollisionIndex, True)
            count += 1

    ListLens.append(count)
