class LRUCache:
    # Thoughts/ideas:
    #  
    # - Use a hash map as cache
    # - Use a linked list as a fifo queue
    # - Instead of storing values directly in cache, store LL nodes in the hash map

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # set up sentinel nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:   
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_end(node)
        return node.val

    def put(self, key: int, val: int) -> None:     
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self._remove(node)
        else:
            node = Node(key, val)
            self.cache[key] = node
        
        self._append(node)

        if len(self.cache) > self.capacity:
            self.cache.pop(self.head.next.key)
            self._remove(self.head.next)

    def _move_to_end(self, node):
        self._remove(node)
        self._append(node)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _append(self, node):
        old_tail = self.tail.prev
        old_tail.next = node
        node.prev = old_tail
        node.next = self.tail
        self.tail.prev = node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None