# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # thoughts/ideas:
        # 
        # find middle, reverse right half, then zip them up

        if not head:
            return None

        length = 1
        c = head
        while c.next:
            c = c.next
            length += 1
        split = (length + 1) // 2 # +1 to keep the extra node in the left half if number of nodes are uneven

        # move b to the head of the right half
        b = head
        for _ in range(split):
            b = b.next

        # cut chain at the end of left half
        a = head
        for _ in range(split - 1):
            a = a.next
        a.next = None
        a = head
        
        # reverse b to end
        prev = None
        cur = b
        while cur:
            if not cur.next: # remember beginning of reversed right half
                b = cur
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # zip
        for i in range(length // 2):
            anext = a.next
            bnext = b.next
            a.next = b
            b.next = anext
            a = anext
            b = bnext

        

# # 2, 4, 6, 8, 10
# a = 2, 4
# b = 10, 8, 6
# middle=2

# 2 -> 10 -> 4
          