class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
        return [int(product / x) for x in nums]