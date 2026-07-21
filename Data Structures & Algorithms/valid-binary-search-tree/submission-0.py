# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = []

        def inorder(node):
            if node is not None:
                inorder(node.left)
                self.result.append(node.val)
                inorder(node.right)

        inorder(root)
        if len(self.result) != len(set(self.result)):
            return False
        else:
            return self.result == sorted(self.result)