from collections import deque

_WATER = -1
_TREASURE = 0
_INF = 2**31 - 1


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # thoughts/ideas:
        #
        # - find all treasures
        # - start a BFS from all treasures to reachable lands, marking the distance

        queue = deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == _TREASURE:
                    queue.append((x, y))

        distance = 0
        while queue:
            distance += 1
            for x, y in [queue.popleft() for _ in range(len(queue))]: # pop all
                for ax, ay in _adjacents(grid, (x, y)):
                    if grid[ax][ay] == _INF:                        
                        grid[ax][ay] = distance
                        queue.append((ax, ay))


def _adjacents(grid, loc):
    x, y = loc
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        ax, ay = x + dx, y + dy
        if 0 <= ax < len(grid) and 0 <= ay < len(grid[0]):
            yield (ax, ay)
