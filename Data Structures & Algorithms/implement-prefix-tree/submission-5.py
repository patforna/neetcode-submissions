# thoughts/ideas
#
# - uses a tree internally
# - root node is empty
# - each node is a char of the string
# - each path from root to leaf represents a valid string or a string starting with if ending at a non-leaf node
# 

class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                child = Node()
                node.children[c] = child
                node = child
        
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
        
    def _find_node(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        
        return node
            








