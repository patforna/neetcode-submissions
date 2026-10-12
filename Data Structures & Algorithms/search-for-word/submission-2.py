class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # thoughts/ideas:
        #
        # find all starting points, i.e. tiles with first letter of word
        # for each, do a dfs

        visited = set()                
        def dfs(x, y, i):
            if (x, y) in visited or board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited.add((x, y))
            found = any([dfs(ax, ay, i + 1) for ax, ay in adjacents(x, y)])
            visited.remove((x, y))

            return found

        def adjacents(x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]):
                    yield (nx, ny)                  

        for x in range(len(board)):
            for y in range(len(board[0])):
                letter = board[x][y]
                if letter == word[0]:                    
                    if dfs(x, y, 0):
                        return True

        return False
