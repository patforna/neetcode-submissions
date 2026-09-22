import heapq
from itertools import count

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # thoughts/ideas:
        # - use a (min) heap of size k
        # - put first node of the k lists on heap
        # - remove top (min) node and replace it with next node
        # - repeat until one node left on heap and append that
        # 
        # Time: O(n * log k). Space: O(k)

        heap = []
        tiebreak = count()
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, next(tiebreak), head))


        dummy = ListNode()
        prev = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            prev.next = node            
            if nxt := node.next:
                heapq.heappush(heap, (nxt.val, next(tiebreak), nxt))
            prev = node

        return dummy.next