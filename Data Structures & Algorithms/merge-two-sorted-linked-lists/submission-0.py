# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 is None):
            if list2 is None:
                return list1
            else: return list2
        if list2 is None:
            return list1
        dummy = ListNode(-1)
        current = dummy
        current1 = list1
        current2 = list2
        while (current1 is not None) or (current2 is not None):
            if  (current1.val <= current2.val):
                current.next = current1
                current1 = current1.next
                if current1 is None:
                    current = current.next
                    current.next = current2
                    break
            elif (current2.val < current1.val):
                current.next = current2
                current2 = current2.next
                if current2 is None:
                    current = current.next
                    current.next = current1
                    break
            current = current.next
        return dummy.next