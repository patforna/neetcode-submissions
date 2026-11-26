"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # thoughts:
    # - deep copy => create new Node / literals / pointers
    # - tricky bit: creating the pointer to random node if it doesn't exist yet
    # - just following random pointers is non-exhaustive
    # - might need two passes or an additional structure to lookup nodes efficiently 

    # ideas:
    # create a map of node -> index for the original list
    # create a map of index -> node for the copied list
    # use these two two resolve the random pointers

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # create node to node copy map (node -> node)
        copies = {}
        node = head
        while node:
            copies[node] = Node(node.val)
            node = node.next

        # resolve and set next and random pointers
        node = head
        while node:
            if node.next:
                copies[node].next = copies[node.next]
            if node.random:
                copies[node].random = copies[node.random]
            
            node = node.next

        return copies[head] if head else None
        
