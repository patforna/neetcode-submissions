class FileSystem:
    # thoughts/ideas:
    #
    # - file paths are paths from the root of a tree down to it's leaves
    # - root is /
    # - values are stored as part of nodes
    # - createpath follows an existing path and checks if it the last segment can be inserted as a child of an existing node
    # - could optimise looking up children by putting them in a hashmap, trading space for time

    def __init__(self):
        self.root = Node("/")        

    def createPath(self, path: str, value: int) -> bool:
        node = self.root
        segments = path.split("/")[1:]
        for segment in segments[0:-1]:
            if segment not in node.children:
                return False # parent path doesn't exist
            node = node.children[segment]
        
        if segments[-1] in node.children:
            return False # path already exists
        
        node.children[segments[-1]] = Node(value)
        return True

    def get(self, path: str) -> int:
        node = self.root
        for segment in path.split("/")[1:]:
            if segment not in node.children:
                return -1 # parent path doesn't exist
            node = node.children[segment]

        return node.val
        
class Node:

    def __init__(self, val):
        self.val = val
        self.children = {}


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
