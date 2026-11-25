# note: not thread-safe
class HitCounter:
    # thoughts:
    # - use a ring buffer with 300 slots - O(1) space
    # - keep track of (timestamp, hits)
    # - make sure to reset when looping around

    def __init__(self):
        self.items = [(0, 0)] * 300    

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.items[i][0] != timestamp:
            self.items[i] = (timestamp, 1)
        else:
            ts, hits = self.items[i]
            self.items[i] = (ts, hits + 1)

    def getHits(self, timestamp: int) -> int:
        return sum(hits for ts, hits in self.items if ts > timestamp - 300)        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
