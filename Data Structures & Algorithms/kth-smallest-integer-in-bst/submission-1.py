# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def postorder(node):
            if node is None:
                return
            
            postorder(node.left)
            self.result.append(node.val)
            postorder(node.right)
        
        postorder(root)
        return self.result[k-1]