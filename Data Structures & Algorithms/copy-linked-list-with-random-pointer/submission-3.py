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
        
        # create node to idx map
        indices = {}
        node = head
        i = 0
        while node:
            indices[node] = i
            i += 1
            node = node.next        

        # create list of node copies
        new_nodes = []
        node = head
        while node:
            new_nodes.append(Node(node.val))
            node = node.next

        # resolve and set next and random pointers
        node = head
        i = 0
        while node:
            if node.next:
                new_nodes[i].next = new_nodes[indices[node.next]]
            if node.random:
                new_nodes[i].random = new_nodes[indices[node.random]]
            
            i += 1
            node = node.next

        return new_nodes[0] if new_nodes else None
        
