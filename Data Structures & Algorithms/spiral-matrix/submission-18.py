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
            # move right along top
            for c in range(left, right):
                result.append(matrix[top][c])
            top += 1

            # move down along right
            for r in range(top, bottom):
                result.append(matrix[r][right - 1])
            right -= 1

            # stop if the layer was a single row or column, so the bottom/left passes don't revisit cells
            if not (top < bottom and left < right):
                break

            # move left along bottom
            for c in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][c])
            bottom -= 1

            # move up along left
            for r in range(bottom - 1, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

        return result
