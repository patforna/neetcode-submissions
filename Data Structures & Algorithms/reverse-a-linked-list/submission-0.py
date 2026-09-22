# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # thoughts/ideas:
        #
        # - maintain two pointers: current and next
        # - point next at current (remembering old values so we can move forward)
        # - move forward
        if head is None:
            return head

        prev = head
        cur = prev.next
        while cur:            
            nxt = cur.next
            
            cur.next = prev
            prev = cur
            cur = nxt
        
        head.next = None
        return prev

# 0 < 1 < 2 < 3   -
#             p   c

# prev=0, cur=1, nxt=2
# prev=0, cur=1, nxt=2