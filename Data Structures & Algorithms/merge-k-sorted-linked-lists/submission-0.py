# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy0 = ListNode(float("-inf"))
        original = dummy0
        for i in range(0,len(lists)):
            if lists[i]:
                dummy1 = ListNode(0)
                current0 = dummy1
                current1 = original
                current2 = lists[i]
                while (current1 is not None) or (current2 is not None):
                    if current1.val <= current2.val:
                        current0.next = current1
                        current1 = current1.next
                        if current1 is None:
                            current0 = current0.next
                            current0.next = current2
                            break
                    elif current1.val > current2.val:
                        current0.next = current2
                        current2 = current2.next
                        if current2 is None:
                            current0 = current0.next
                            current0.next = current1
                            break
                    current0 = current0.next
                dummy1 = dummy1.next
                original = dummy1
        return original.next