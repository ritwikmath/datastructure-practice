class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 if not list2 else list2

        newList = returnList = ListNode()
        while list1 or list2:
            value: int = 0
            if not list2 or (list1 and list1.val <= list2.val):
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            newList.next = ListNode(value)
            newList = newList.next
        return returnList.next
