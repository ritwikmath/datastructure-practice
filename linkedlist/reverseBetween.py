from typing import Optional
from linkedlist import l as linkedllist, Node

class Solution:
    def reverseBetween(self, head: Optional[Node], left: int, right: int) -> Optional[Node]:
        # First edge case -> If linkedlist is empty
        if head is None:
            print("Linkedlist is empty")
            return

        count: int = 1
        current: Node = head
        previous: Optional[Node] = None
        reverse_node_end: Optional[Node] = None
        left_pointer: Optional[Node] = None
        while(current is not None):
            next_node = current.next
            if left != 1 and count == left - 1:
                left_pointer = current
            if count >= left and count <= right:
                if count == left:
                    reverse_node_end = current
                if count is right:
                    if left_pointer:
                        left_pointer.next = current
                    reverse_node_end.next = current.next
                    if left == 1:
                        head = current
                current.next = previous
                previous = current
            current = next_node
            count += 1
            
        return head

if __name__ == '__main__':
    linkedllist.addAtBeginning(0)
    linkedllist.addAtLast(6)
    linkedllist.addAtLast(7)
    linkedllist.head = Solution().reverseBetween(linkedllist.head, 1, 7)
    linkedllist.printList()