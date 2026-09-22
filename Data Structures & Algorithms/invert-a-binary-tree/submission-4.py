# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTreeRec(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # thoughts/ideas:
        # 
        # - recursive solution probably reads best
        # - if root is None, return None
        # - otherwise, swap left and right child and call invertTree on both of them
        # drawback: uses O(n) space (tree/stack height) - O(n) because that's the worst case height of a BT
        if not root:
            return None

        x = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(x)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # thoughts/ideas:
        #
        # - push children onto a stack (DFS) or queue (BFS)
        
        queue = deque([root]) # should use something that supports O(1) removal from the head (e.g. linked list) - don't remember api syntax
        while queue:            
            n = queue.popleft()
            if n:
                queue.extend([n.left, n.right])
                x = n.left
                n.left = n.right
                n.right = x

        return root