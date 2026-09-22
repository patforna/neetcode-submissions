# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists_(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        # thoughts/ideas:
        # - two pointers, one for each list
        # - compare values, swap in smaller one and move pointer to its next node
        # - when one list finished, append the rest of the other list

        if a is None:
            return b
        
        if b is None:
            return a

        if a.val <= b.val:
            head = a
            a = a.next
        else:
            head = b
            b = b.next

        cur = head
        while a and b:
            if a.val <= b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next

            cur = cur.next

        cur.next = a or b

        return head 

    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy
        cur = dummy

        while a and b:
            if a.val <= b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next

            cur = cur.next

        cur.next = a or b

        return dummy.next
