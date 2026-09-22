# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTreeRec(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
        