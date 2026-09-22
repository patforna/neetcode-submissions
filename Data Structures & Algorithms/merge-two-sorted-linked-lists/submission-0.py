# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
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

        cur.next = a if a else b

        return head 

# a=1,1(b),2,4
#       ^
# b=1,3,5
#   ^

# head=1(a)
# cur=1(a)
