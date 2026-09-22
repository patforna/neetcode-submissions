# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # thoughts/ideas:
        # - two pointers
        # - advance one by n
        # - when advanced one reaches end, the other one is on -n -> remove
        # - (edge cases)

        dummy = ListNode(next=head)

        a = dummy
        b = dummy
        for _ in range(n + 1):
            b = b.next

        while b:
            a = a.next
            b = b.next

        a.next = a.next.next

        return dummy.next
        
# list=d,1,2
# a    ^
# b          ^
