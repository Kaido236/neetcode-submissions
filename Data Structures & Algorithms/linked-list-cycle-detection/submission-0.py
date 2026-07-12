# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        back = False
        current = head
        hash_node = {}
        while current is not None:
            if current in hash_node:
                return True
            else:
                hash_node[current] = True
            current = current.next
        return False
        