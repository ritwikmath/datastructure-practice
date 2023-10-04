from typing import Optional
from linkedlist import l as linkedllist, Node

class Solution:
    def reverseBetween(self, head: Optional[Node], left: int, right: int) -> Optional[Node]:
        # First edge case -> If linkedlist is empty
        if head is None:
            print("Linkedlist is empty")
            return

        count: int = 1
        left_pointer: Optional[Node] = None
        new_head: Optional[Node] = None
        previous: Optional[Node] = None
        while(head is not None):
            reverse_node_end: Optional[Node] = None 
            if count >= left and count <= right:
                if count == left:
                    reverse_node_end = head
                    continue
                next_node = head.next
                head.next = previous
                previous = head
                if count is right:
                    reverse_node_end.next = next_node
            head = next_node
            count += 1
            
        
        return head

if __name__ == '__main__':
    linkedllist.head = Solution().reverseList(linkedllist.head)
    linkedllist.printList()