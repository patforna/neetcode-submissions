# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # thoughts/ideas:
        # - bfs or dfs keeping track of max
        # - we'll go with dfs

        md = 0
        stack = [(1, root)]
        while stack:
            d, n = stack.pop()
            if n:
                md = max(d, md)
                stack.extend([(d + 1, n.left), (d + 1, n.right)])
        
        return md
                        


# stack=[(1,1)], n=1, d=1, md=1
# stack=[(2,2), (2,3)], n=3, d=2, md=2
# stack=[(2,2), (3,4), (3,None)], n=None, d=3
# stack=[(2,2), (3,4)], n=4, d=3, md=3
