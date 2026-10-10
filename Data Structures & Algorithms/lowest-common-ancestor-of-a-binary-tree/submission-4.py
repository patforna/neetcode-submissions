# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # thoughts/ideas: 
        # - recursively call lca on left and right subtree to find p and q (semantically overloaded)
        # - if neither p nor q found, return none
        # - if subtree root is p or q, return it (ancestor can't be lower than p or q itself)
        # - if p are q are split between left and right subtree, return root (lca is before the split)

        if not root or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


    

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
            return [a] + pl # issue: this is O(n) in itself, which makes the whole thing O(n^2)
        pr = self._path(a.right, b)
        if pr: 
            return [a] + pr
        
        return None

# path(5, 1)=[5,3,1]
#   path(3, 1)=[3,1]
#     path(2, 1)=None    path(1, 1)=[1]
#       path(None, 1)=None      path(None, 1)=None
