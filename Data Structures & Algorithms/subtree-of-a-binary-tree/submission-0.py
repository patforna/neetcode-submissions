from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        # thought/ideas:
        # - two steps:
        #   1. find subroot(s) in root tree
        #   2. check if subtrees are equal
        # Time: O(n * m) where n is number of nodes in root tree and m is number of nodes in subroot tree

        sub_trees = [] # candidates
        queue = deque([root])
        while queue:
            n = queue.popleft()
            if n:
                if n.val == sub_root.val:
                    sub_trees.append(n)
                queue.extend([n.left, n.right])

        for st in sub_trees:
            if is_equal(st, sub_root):
                return True

        return False

    
def is_equal(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    qa = deque([a])
    qb = deque([b])

    while qa and qb:
        na = qa.popleft()
        nb = qb.popleft()

        nav = na.val if na else None
        nbv = nb.val if nb else None

        if nav != nbv:
            return False
        
        if na:
            qa.extend([na.left, na.right])
            qb.extend([nb.left, nb.right])
        
    return len(qa) == len(qb)
