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

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    def invertTreeItBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # thoughts/ideas:
        #
        # - iteratively add children to a queue (BFS)
        
        queue = deque([root])
        while queue:            
            n = queue.popleft()
            if n:
                queue.extend([n.left, n.right])
                n.left, n.right = n.right, n.left

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # thoughts/ideas:
        #
        # - push children onto a stack (DFS)

        stack = []
        n = root
        while stack or n:
            if n:
                stack.append(n)
                n = n.left
            else:
                n = stack.pop()
                n.left, n.right = n.right, n.left
                n = n.left # i.e. the old right...                    
        
        return root


            





