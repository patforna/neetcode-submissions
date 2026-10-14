from functools import cache

class Solution:

    @cache
    def climbStairsRec(self, n: int) -> int:
        # n == number of steps
        # steps at a time: 1 or 2
        # wanted: number of distinct ways to go to n
        # thoughts/ideas:
        # recursion:
        # for n 2 1:
        #   ways to reach n = ways to reach n-1 + ...n-2
        # cache result so we don't compute the same result twice
        # for n(1) = 1, n(2) = 2
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        u, v = 1, 2
        for i in range(3, n):
            u, v = v, u + v

        return u + v


# n=3 r=3
#   c(2)=2 + c(1)=1

# n=4 r=5
#   c(3)=3 + c(2)=2
    