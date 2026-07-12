"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        hash_node = {None:None}
        while current is not None:
            hash_node[current] = Node(current.val)
            current = current.next
        current = head
        while current is not None:
            hash_node[current].next = hash_node[current.next]
            hash_node[current].random = hash_node[current.random]
            current = current.next
        return hash_node[head]