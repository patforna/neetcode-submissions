class Node:
    def __init__(self, timestamp=-1, hits=-1, next=None):
        self.timestamp = timestamp
        self.hits = hits
        self.next = next    

class HitCounter:

    MAX_AGE = 300

    # thoughts:
    # - use a fixed number (300) of buckets - one for each second - O(1) space
    # - chain them up as a linked list
    def __init__(self):
        self.head = Node() # sentinel
        self.tail = self.head

    def hit(self, timestamp: int) -> None:
        if self.tail.timestamp == timestamp:
            self.tail.hits += 1
        else:
            self.tail.next = Node(timestamp, hits=1)
            self.tail = self.tail.next    

        self.drop_old(timestamp - self.MAX_AGE)                    

    def getHits(self, timestamp: int) -> int:
        self.drop_old(timestamp - self.MAX_AGE)

        hits = 0
        node = self.head.next
        while node:
            hits += node.hits
            node = node.next

        return hits

    def drop_old(self, limit: int) -> None:
        node = self.head.next
        while node and node.timestamp <= limit:
            self.head.next = node.next
            node = node.next
        
        if not self.head.next:
            self.tail = self.head

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
