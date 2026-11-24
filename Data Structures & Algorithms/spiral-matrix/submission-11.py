class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # thoughts/ideas:
        # - m = rows, n = cols
        # - 4 pointers: top, left, right, bottom
        # - shrink pointers whenever a row or col is complete
        # - stop when top/bottom or left/right meet
        # - Time: O(m*n), Space: O(1)

        result = []

        # for convenience
        m = len(matrix)
        n = len(matrix[0])

        # top and left are inclusive, right and bottom are exclusive
        top, left, right, bottom = 0, 0, n, m

        while top < bottom and left < right:
            row, col = top, left # starting point

            # move right
            for c in range(left, right):
                result.append(matrix[top][c])
            
            while col < right:
                # result.append(matrix[row][col])
                col += 1
            col -= 1
            top += 1
            row += 1
            
            # move down
            while row < bottom:
                result.append(matrix[row][col])
                row += 1
            row -= 1
            right -= 1
            col -= 1            

            if not (top < bottom and left < right):
                break

            # move left
            while col >= left:
                result.append(matrix[row][col])
                col -= 1
            col += 1
            bottom -= 1
            row -= 1

            # move up
            while row >= top:
                result.append(matrix[row][col])
                row -= 1
            left += 1

        return result
