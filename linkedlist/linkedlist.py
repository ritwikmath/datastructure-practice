from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

@dataclass
class Node:
    value: str | int
    next: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
    
    def addAtBeginning(self, data) -> Node:
        if (self.head is None):
            self.head = Node(data)
            return self.head
        
        node = Node(data)
        node.next = self.head
        self.head = node
        return self.head
    
    def addAtLast(self, data) -> None:
        if (self.head is None):
            self.head = Node(data)
            return
        
        current = self.head
        while(current is not None):
            if (current.next is None):
                node = Node(data)
                current.next = node
                break
            current = current.next
    
    def printList(self):
        current = self.head
        while(current is not None):
            print(current.value)
            current = current.next
        print('Lined list traverse complete')

l = LinkedList()
l.addAtBeginning(4)
l.addAtBeginning(3)
l.addAtBeginning(2)
l.addAtBeginning(1)
l.addAtLast(5)
if __name__ == '__main__':
    l.printList()