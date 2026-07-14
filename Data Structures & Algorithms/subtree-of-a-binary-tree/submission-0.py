# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a,b):
            if a is None and b is None:
                return True
            
            if a is None or b is None:
                return False
            
            return a.val == b.val and isSameTree(a.right,b.right) and isSameTree(a.left,b.left)

        if root is None:
            return False
        
        if subRoot is None:
            return True
        
        if isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)