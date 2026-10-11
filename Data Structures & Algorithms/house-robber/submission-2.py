from functools import cache

class Solution:

    def rob(self, nums: List[int]) -> int:
        # thoughts/ideas:
        #
        # - pick first or second house
        # - then, for each choice, recursively pick i + 2 and i + 3 (no need to pick more, because result can only be worse as i+2 or i+3
        #   could be included and is positive)
        # - cache the solutions so we don't recompute the same things twice

        @cache
        def _rob(i):
            if i >= len(nums):
                return 0
            
            if i + 1 == len(nums):
                return nums[i]

            if i + 2 == len(nums):
                return max(nums[i], nums[i + 1])

            first = nums[i] + _rob(i + 2)
            second = nums[i + 1] + _rob(i + 3)

            return max(first, second)

        return _rob(0)