# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # thoughts/ideas:
        # - bfs, level by level in one swoop
        result = []
        queue = deque([root])
        while queue:
            nodes = []
            while queue:
                n = queue.popleft()
                if n:
                    nodes.append(n)

            if nodes:
                result.append([n.val for n in nodes])
            
            # add children to queue
            for n in nodes:
                queue.append(n.left)
                queue.append(n.right)
            
        return result

# trace
# queue=[1], nodes=[], nodes=[1], queue=[], result=[[1]], n=1, queue=[2, 3]
# queue=[2,3], nodes=[], nodes=[2,3], queue=[], result=[[1], [2,3]], n=2, queue=[4, 5], n=3, queue=[4,5,6,7]
# queue=[4,5,6,7], nodes=[], nodes=[4,5,6,7], queue=[], result=[[1],[2,3],[4,5,6,7]]
