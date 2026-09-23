from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # thoughts/ideas:
        # 
        # tree = acyclic graph
        # assumption: single tree (not forest of trees) -> connected graph
        # 
        # - start at any node
        # - walk the graph (e.g. BFS), tracking which nodes have already been visited
        # - if re-visiting -> cycle -> not a tree
        # - at the end, check that graph is connected, i.e. visited nodes - 1 == number of edges

        if not edges:
            return True
        
        # build adjacency list for easier access 
        adjacents = defaultdict(list)
        for a, b in edges:
            adjacents[a].append(b)
            adjacents[b].append(a) # both ways becuase undirected
        
        visited = set()
        root = (-1, edges[0][0]) # (parent, node)
        queue = deque([root])
        while queue:
            parent, node = queue.popleft()

            if node in visited:
                return False
            visited.add(node)
            queue.extend([(node, a) for a in adjacents[node] if a != parent]) # !!! exclude link back to parents to avoid a<->b type cycles

        return len(visited) == n
