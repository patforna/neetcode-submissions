from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTreeRec(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        pv = p.val if p else None
        qv = q.val if q else None
        if pv != qv:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # thoughts/ideas:
        #
        # - walk both trees simultaneously and compare nodes

        qp = deque([p])
        qq = deque([q])
        
        while qp and qq:
            np = qp.popleft()
            nq = qq.popleft()

            npv = np.val if np else None
            npq = nq.val if nq else None

            if npv != npq:
                return False

            if np:
                qp.extend([np.left, np.right])
                qq.extend([nq.left, nq.right])
        
        return len(qp) == len(qq)

# qp.pop  qq.pop  qp      qq
#                 [1]     [1]
# 1       1       [2,3]   [2,3]
