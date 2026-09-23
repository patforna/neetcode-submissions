from collections import deque

_LAND = "1"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # thoughts/ideas:
        # - go through grid
        # - when encountering land (1), find all connected land (BFS)
        # - remember all land that has been visited
        #   - if we can mutate the input, we could do this in-place by zero-ing out the land
        #   - otherwise, just maintain a dict - O(n) space
        # - continue going through grid
        # - don't re-explore land we already explored as part of a previous exploration
        # - count number of islands

        visited = set()
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == _LAND and (x, y) not in visited:
                    count += 1
                    queue = deque([(x, y)])
                    visited.add((x, y))
                    while queue:
                        loc = queue.popleft()
                        for ax, ay in _adjacents(grid, loc):
                            if grid[ax][ay] == _LAND and (ax, ay) not in visited:
                                visited.add((ax, ay))
                                queue.append((ax,ay))

        return count

def _adjacents(grid: List[List[str]], loc: Tuple[int, int]) -> List[Tuple[int, int]]:
    result = []
    x, y = loc
    if x + 1 < len(grid):
        result.append((x + 1, y))
    if x - 1 >= 0:
        result.append((x - 1, y))
    if y + 1 < len(grid[0]):
        result.append((x, y + 1))
    if y - 1 >= 0:
        result.append((x, y - 1))
    
    return result


# trace
# x=0, y=0, grid[x][y]="0", visited={}
# x=0, y=1            ="1", count=1, queue=[(0,1)]
#   loc=(0,1), queue=[], visited={(0,1)}, queue=[(0,2),(1,1)]
#   loc=(0,2), 
