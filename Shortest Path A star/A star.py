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

shortest_path = []

class Node:
    
    def __init__(self, f_val, DistanceTravelled, previous_node, h, adjacentNodes, index, obj):
        

        self.f_val = f_val
        self.DistanceTravelled = DistanceTravelled
        self.previous_node = previous_node
        self.h = h
        self.adjacentNodes = adjacentNodes
        self.index = index
        self.obj = obj



def MapPath(node):
    
    shortest_path.append(node.obj)
    if node.previous_node == None:
        return
    MapPath(node.previous_node)


def main():
    
    Node_list = []

    for i in range(adjacentNodes_i.BranchCount):
        adjacentNodes = adjacentNodes_i.Branch(i)
        Node_list.append(Node( 0, 0, None, Heuristic_weight[i], adjacentNodes, i, nodes[i]))

    OpenNodes = []
    ClosedNodes = []

    currentNode = Node_list[startPoint_i]
    OpenNodes.append(currentNode)



    AdjNodes = currentNode.adjacentNodes
    

    while True:
    
    
        for adj_node_i in AdjNodes:
    
            adj_node = Node_list[ adj_node_i ]
    
            if adj_node not in ClosedNodes:
        
                h = adj_node.h
                node = adj_node.obj
                g = ghc.Distance( currentNode.obj, node ) + currentNode.DistanceTravelled
                f_new = g + h
                f_current = adj_node.f_val
        
                if f_current > f_new or f_current == 0:
                    adj_node.f_val = f_new
                    adj_node.previous_node = currentNode
                    adj_node.DistanceTravelled = g
            
                if adj_node not in OpenNodes:
                    OpenNodes.append(adj_node)

        ClosedNodes.append(currentNode)
        OpenNodes.remove(currentNode)

        currentNode = sorted(OpenNodes, key=lambda node: node.f_val, reverse=True)[len(OpenNodes)-1]

        if currentNode.index == endPoint_i:
            
            MapPath(currentNode)
            break
        AdjNodes = currentNode.adjacentNodes


if __name__=="__main__":
    main()







