# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # thoughts
    # - use recursion
    # - base condition == null
    # - adjust low, high bounds when recursing
    #   - if going left, tighten mx bound (all must be smaller than ...)
    #   - if going right, tighten mn found (all must be larger than ...)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, mn, mx):
            if not node:
                return True

            if node.val <= mn or node.val >= mx:
                return False
        
            return is_valid(node.left, mn, node.val) and is_valid(node.right, node.val, mx)

        return is_valid(root, float("-inf"), float("inf"))

# n=1, mn=-inf, mx=inf
#   n=2, mn=-inf, mx=1