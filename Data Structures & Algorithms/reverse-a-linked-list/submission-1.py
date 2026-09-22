# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList_(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev