# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        queue = [root]
        future_queue = []
        if root.left is not None:
            future_queue.append(root.left)
        if root.right is not None:
            future_queue.append(root.right)
        while future_queue:
            queue = future_queue
            depth += 1
            future_queue = []
            for node in queue:
                if node.left is not None:
                    future_queue.append(node.left)
                if node.right is not None:
                    future_queue.append(node.right)
        return depth
        