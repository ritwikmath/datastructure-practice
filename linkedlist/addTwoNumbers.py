from typing import Optional
from linkedlist import l as linkedllist, Node

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return
        newList: ListNode = ListNode()
        head = newList
        carry: int = 0
        
        while l1 or l2 or bool(carry):
            first_digit: int = l1.val if l1 else 0
            second_digit: int = l2.val if l2 else 0
            num: int = (value := (first_digit + second_digit + carry)) % 10
            carry: int = value // 10
            head.next: ListNode = ListNode(num)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return newList.next