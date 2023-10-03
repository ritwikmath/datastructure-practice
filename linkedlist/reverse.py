from typing import Optional
from linkedlist import l as linkedllist, Node

class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        # First edge case -> If linkedlist is empty
        if head is None:
            print("Linkedlist is empty")
            return

        new_head: Optional[Node] = None 
        previous: Optional[Node] = None
        while(head is not None):
            next_node = head.next
            head.next = previous
            previous = head
            head = next_node
            if head is None:
                new_head = previous
        
        return new_head

if __name__ == '__main__':
    linkedllist.head = Solution().reverseList(linkedllist.head)
    linkedllist.printList()