class Solution:
    def productExceptSelf_(self, nums: List[int]) -> List[int]:
        import math

        # thoughts/ideas (with division):
        # - compute product over entire list
        # - map over list, replacing each item with product divided by list item

        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            output = [0] * len(nums)
            output[nums.index(0)] = math.prod([x for x in nums if x != 0])
            return output

        product = math.prod(nums)
        return [product // x for x in nums]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # thoughts/ideas (without division):
        # for each i in nums[i]
        #   incrementally compute product on the left of i
        #   incrementally compute product on the right of i  -- O(n) time and space
        #
        # for each i in nums[i]
        #   compute product by multiplying the two products @ i avoe -- O(n) time
        if len(nums) <= 1:
            return []

        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [l * r for l, r in zip(left, right)]
