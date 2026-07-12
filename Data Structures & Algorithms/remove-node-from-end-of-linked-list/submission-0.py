# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        current = head
        lenght = 1
        while current.next is not None:
            lenght += 1
            current = current.next
        n = lenght - n
        if n == 0:
            head = head.next
            return head
        p = 0
        current = head
        while current is not None:
            if p < n-1:
                p += 1
            else:
                future = current.next
                current.next = future.next
                break
            current = current.next
        return head