# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # thoughts/idea:
        # - "go down" recursively calling lca on the left and right branch.
        # - stop when one of the branches returns none -> the root/node at that level is the lca
        
        if not root:
            return None
        
        if not root or root is p or root is q:
            return root
        
        al = self.lowestCommonAncestor(root.left, p, q)
        ar = self.lowestCommonAncestor(root.right, p, q)

        if al and ar:
            return root

        return al or ar


    def lowestCommonAncestor_(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # thoughts/ideas:
        # - generate path from root for nodes: O(n)
        # - then walk path from left to right and return last node that matches before paths diverge: O(h)

        path_p = self._path(root, p)
        path_q = self._path(root, q)

        lowest = root
        for i in range(len(path_p)):
            if len(path_q) <= i or path_p[i].val !=  path_q[i].val:
                break
            lowest = path_p[i]

        return lowest

    def _path(self, a, b):        
        if not a:
            return None

        if a is b:
            return [a]

        pl = self._path(a.left, b)
        if pl:
            return [a] + pl
        pr = self._path(a.right, b)
        if pr: 
            return [a] + pr
        
        return None

# path(5, 1)=[5,3,1]
#   path(3, 1)=[3,1]
#     path(2, 1)=None    path(1, 1)=[1]
#       path(None, 1)=None      path(None, 1)=None
