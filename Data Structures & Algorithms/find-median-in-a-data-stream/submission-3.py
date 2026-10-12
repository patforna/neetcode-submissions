import heapq

class MedianFinder:
    # thoughts/ideas:
    # - median is always in the middle(-ish) of a sorted list
    # - idea:
    #   - separate the list into two halves
    #   - use a max heap on the left, a min heap on the right
    #   - keep them balanced-ish
    #   - find the median by peeking at the top of the heaps

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (-self.left[0] + self.right[0]) / 2
        