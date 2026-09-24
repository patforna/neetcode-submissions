from collections import deque

_LAND = 1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # thoughts/ideas
        # - walk through grid
        # - if land found, find the rest of the land (BFS)
        # - keep track of max land size
        # - do not revisit visited land

        max_area = 0
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == _LAND and (x, y) not in visited:
                    visited.add((x, y))
                    queue = deque([(x, y)])
                    area = 0
                    while queue:
                        loc = queue.popleft()
                        area += 1
                        for ax, ay in _adjacents(grid, loc):
                            if grid[ax][ay] == _LAND and (ax, ay) not in visited:
                                visited.add((ax, ay))
                                queue.append((ax, ay))
                    
                    max_area = max(area, max_area)
        
        return max_area

def _adjacents(grid, loc):
    x, y = loc
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ax, ay = x + dx, y + dy
        if 0 <= ax < len(grid) and 0 <= ay < len(grid[0]):
            yield (ax, ay)