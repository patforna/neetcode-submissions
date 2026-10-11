from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robbers_one(nums[1:]), self.robbers_one(nums[:-1]))
        

    def robbers_one(self, nums: List[int]) -> int:
        @cache
        def _rob(i):
            if i >= len(nums):
                return 0
            
            first = nums[i] + _rob(i + 2)
            second = _rob(i + 1)

            return max(first, second)

        return _rob(0) 