from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # thoughts/ideas:
    # - recursively calling maxDepth on left and right subtree and taking max
    # - bfs or dfs keeping track of depth and max depth

    def maxDepthRec(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepthRec(root.left), self.maxDepthRec(root.right)) + 1    
    
    def maxDepthBfs(self, root: Optional[TreeNode]) -> int:
        md = 0
        queue = deque([(1, root)])
        while queue:
            d, n = queue.popleft()
            if n:
                md = max(d, md)
                queue.extend([(d + 1, n.left), (d + 1, n.right)])
            
        return md                

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        nodes = [root]
        while nodes:
            nxt = [n for n in nodes if n]
            nodes = []
            if nxt:
                depth += 1
                for n in nxt:
                    nodes.extend([n.left, n.right])

        return depth

    def maxDepthDfs(self, root: Optional[TreeNode]) -> int:
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
