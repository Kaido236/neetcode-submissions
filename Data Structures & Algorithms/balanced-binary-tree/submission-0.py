# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if node is None:
                return 0
        
            left = 1 + depth(node.left)
            right = 1+ depth(node.right)

            return max(left,right)

        if root is None:
            return True

        if root.left is not None:
            left = depth(root.left)
        else:
            left = 0

        if root.right is not None:
            right = depth(root.right) 
        else:
            right = 0

        return (abs(left-right) <= 1) and self.isBalanced(root.right) and self.isBalanced(root.left)