import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lenght = 0
        current = head
        while current is not None:
            lenght += 1
            current = current.next
        boundary = math.ceil(lenght/2)
        current = head
        p = 0
        while current is not None:
            p += 1
            if p== boundary:
                future = current.next
                current.next = None
                break
            current = current.next
        current1 = head
        previous = None
        current_reverse = future
        while current_reverse is not None:
            future = current_reverse.next
            current_reverse.next = previous
            previous = current_reverse 
            current_reverse = future
        current2 = previous
        list_merge = ListNode(0)
        head_merge = list_merge
        swap = True
        while (current1 is not None) or (current2 is not None):
            if swap:
                list_merge.next = current1
                current1 = current1.next
                swap = False
            else:
                list_merge.next = current2
                current2 = current2.next
                swap = True
            list_merge = list_merge.next
        list_merge.next = None
        head_merge = head_merge.next
        head = head_merge