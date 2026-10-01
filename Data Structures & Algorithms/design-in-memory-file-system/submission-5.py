# thoughts/ideas:
# - use a tree internally
# - root at /
# - dir and file nodes
# - path from root down the tree is a file path
# - sort lexicographically when listing paths

# later: optimising lexicographic sorting

class FileSystem:

    def __init__(self):
        self.root = Node()                

    def ls(self, path):
        node = self._node_at(path)
        if node.is_file:
            return [self._segments(path)[-1]]
        else:
            return sorted(node.children.keys())
        

    def mkdir(self, path):
        node = self.root
        for seg in self._segments(path):
            if seg in node.children:
                node = node.children[seg]
            else:
                child = Node()
                node.children[seg] = child
                node = child

    def addContentToFile(self, file_path, content):
        node = self.root
        segments = self._segments(file_path)
        for seg in segments[:-1]:
            node = node.children[seg]
        
        file_name = segments[-1]
        if file_name in node.children:
            node.children[file_name].content += content
        else:
            node.children[file_name] = Node(content, is_file=True)        

    def readContentFromFile(self, file_path):
        return self._node_at(file_path).content

    def _segments(self, path):
        return [p for p in path.split("/") if p]

    def _node_at(self, path):
        node = self.root
        segments = self._segments(path)
        for seg in segments:
            node = node.children[seg]

        return node

class Node:
    def __init__(self, content=None, is_file=False):
        self.content = content
        self.is_file = is_file
        self.children = {}

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
