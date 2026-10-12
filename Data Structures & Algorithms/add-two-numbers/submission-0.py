# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # thoughts/ideas:
        # - walk left to right
        # - add + remember carry
        # 
        # also consider case where l1 and l2 are not same length

        carry = 0        
        head = ListNode()
        node = head
        while l1 or l2:   
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            carry = 1 if total > 9 else 0

            node.next = ListNode(total % 10)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            node.next = ListNode(1)

        return head.next