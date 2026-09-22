# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # idea:
        # - use two pointers
        # - move one forward at double speed
        # - if the end is reached -> no cycle
        # - if they meet -> cycle

        if head is None:
            return False

        a = head
        b = head.next
        while a != b:
            a = a.next
            if b is None or b.next is None:
                return False
            else:
                b = b.next.next

        return True