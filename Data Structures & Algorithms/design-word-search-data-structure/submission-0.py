# thoughts/ideas:
# - use a trie
# - each character is a node
# - paths from root to a leaf represent valid words
# - tweak on search: when encountering a `.` explore all possible paths from and return if any of them lead to a leaf


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
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
        return self._search(word, self.root)

    def _search(self, word, start):
        node = start
        for i, c in enumerate(word):
            if c == ".":
                return any(self._search(word[i + 1:], child) for child in node.children.values())
            elif c in node.children:
                node = node.children[c]
            else:
                return False

        return node.is_word


class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
