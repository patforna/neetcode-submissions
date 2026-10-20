from collections import deque
from threading import Lock

class HitCounter:
    # thoughts:
    # - use a linked list of up to 300 buckets
    # - on hit(), either increment latest bucket or add a new bucket
    # - on getHits(), drop buckets older than timestamp - 300
    # - maintain a sliding window counter

    def __init__(self):
        self.buckets = deque()
        self.hits = 0
        self.lock = Lock()
        
    def hit(self, timestamp: int) -> None: # not thread-safe!
        with self.lock:
            if self.buckets and self.buckets[-1][0] == timestamp:
                last_ts, last_val = self.buckets[-1]
                self.buckets[-1] = (timestamp, last_val + 1)
            else:
                self.buckets.append((timestamp, 1))
        
        self.hits += 1

    def getHits(self, timestamp: int) -> int:
        with self.lock:
            while self.buckets and self.buckets[0][0] <= timestamp - 300:
                _, hits = self.buckets.popleft()
                self.hits -= hits
            
            return self.hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# h(1), [(1,1)], hits=1
# h(2), [(1,1), (2,1)], hits=2
# h(3), [(1,1), (2,1), (3,1)], hits=3
# gh(4) -> 3
# h(300), [(1,1), (2,1), (3,1), (300, 1)], hits=4
# h(301), [(2,1), (3,1), (300, 1)], hits=3

# [(1, 1), (2, 1)]