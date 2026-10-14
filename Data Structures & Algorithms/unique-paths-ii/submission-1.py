from functools import cache

FREE = 0

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        # robot. start: top left
        # goal: bottom-right
        # m x n grid
        # can only move down or right
        # obstacles == 1

        # wanted: **number** of possible unique paths

        # thoughts/ideas:
        # dfs, accumulating paths. issue, same sub-paths explored multiple times
        
        # other approach: recursion and cache number of possible paths from (x,y)

        if not grid or not grid[0] or grid[0][0] != FREE:
            return 0

        @cache
        def paths(x, y):
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return 1

            result = 0
            for ax, ay in self._adjacents(grid, x, y):
                result += paths(ax, ay)
            return result

        return paths(0, 0)
        
    def _adjacents(self, grid, x, y):
        for nx, ny in ((x + 1, y), (x, y + 1)):
            if nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == FREE:
                yield nx, ny


# p(0,0)
#  p(1,0) + p(0,1)
#    p(2,0) + 
