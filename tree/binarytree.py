from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class Node:
    value: int
    left: None | Node = None
    right: None | Node = None

class BinaryTree:
    root: None | Node = None
    counter: int = -1

    def preeOrderBuild(self, nodes: List[int]) -> None | Node:
        try:
            self.counter += 1
            if nodes[self.counter] == None:
                return
            
            newNode = Node(nodes[self.counter]) 
            
            if self.root is None:
                self.root = newNode
            
            newNode.left = self.preeOrderBuild(nodes)
            newNode.right = self.preeOrderBuild(nodes)

            return newNode
        except IndexError:
            return

    def preeOrderTraversal(self, node: None | Node):
        if not node:
            return
        print(node.value, end=",")
        self.preeOrderTraversal(node.left)
        self.preeOrderTraversal(node.right)
    
    def postOrderTraversal(self, node: None | Node):
        if not node:
            return
        
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node.value, end=",")
    
    def postOrderTraversal(self, node: None | Node):
        if not node:
            return
        
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node.value, end=",")
    
    def inOrderTraversal(self, node: None | Node):
        if not node:
            return
        
        self.postOrderTraversal(node.left)
        print(node.value, end=",")
        self.postOrderTraversal(node.right)
    
tree = BinaryTree()
tree.preeOrderBuild([0,1,None,None,2])
tree.preeOrderTraversal(tree.root)
print("")
tree.postOrderTraversal(tree.root)
print("")
tree.inOrderTraversal(tree.root)