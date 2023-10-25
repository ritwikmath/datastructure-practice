from typing import Optional
from linkedlist import LinkedList, Node

class Solution:
    def addTwoNumbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        if not l1 or not l2:
            return
        newList: LinkedList = LinkedList()
        carry: int = 0
        
        while l1 or l2 or bool(carry):
            first_digit: int = l1.value if l1 else 0
            second_digit: int = l2.value if l2 else 0
            num: int = (value := (first_digit + second_digit + carry)) % 10
            carry: int = value // 10
            newList.addAtLast(num)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return newList

if __name__ == '__main__':
    l1 = LinkedList()
    l1.addAtBeginning(1)
    l1.addAtLast(9)
    l2 = LinkedList()
    l2.addAtBeginning(1)
    l2.addAtLast(1)
    l2.addAtLast(2)
    l3 = Solution().addTwoNumbers(l1.head, l2.head)
    l3.printList()
    