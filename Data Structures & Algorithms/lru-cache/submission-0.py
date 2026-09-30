class LRUCache:
    # thoughts/ideas:
    # - use a hash map
    # - instead of adding values directly, add the nodes of a linked list
    # - then, on get() and put(), move the nodes of the ll accordingly
    # - if list 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # set up sentinels
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def get(self, key: int) -> int:        
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        self._remove(node)
        self._append(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
        else:
            node = self.cache[key]
            node.val = value
            self._remove(node)
        
        node = self.cache[key]
        self._append(node)
        
        if len(self.cache) > self.capacity:
            old_node = self._popleft()
            self.cache.pop(old_node.key)

    def _remove(self, node):  
        a = node.prv
        c = node.nxt
        a.nxt = c
        c.prv = a
        node.prv = None
        node.nxt = None

    def _append(self, node):        
        old_tail = self.tail.prv
        old_tail.nxt = node
        node.prv = old_tail
        node.nxt = self.tail
        self.tail.prv = node

    def _popleft(self):
        old_head = self.head.nxt
        self._remove(old_head)
        return old_head

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = None
        self.nxt = None