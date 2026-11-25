from collections import deque

class HitCounter:
    # thoughts/ideas:
    # - use a linked list (deque) to keep track of up to last 300 hits/sec - O(1) space
    # - use it as a sliding window to maintain count

    def __init__(self):
        self.items = deque() # [timestamp, hits]

    def hit(self, timestamp: int) -> None:
        if self.items and self.items[-1][0] == timestamp:
            self.items[-1][1] += 1
        else:            
            self.items.append([timestamp, 1])

        self._expire(timestamp - 300)

    def getHits(self, timestamp: int) -> int:
        self._expire(timestamp - 300)        
        return sum(hits for _, hits in self.items)
    
    def _expire(self, limit):
        while self.items and self.items[0][0] <= limit:
            self.items.popleft()

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
