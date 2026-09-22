# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # thoughts/ideas:
        # 
        # - recursive solution probably reads best
        # - if root is None, return None
        # - otherwise, swap left and right child and call invertTree on both of them
        if not root:
            return None

        x = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(x)

        return root