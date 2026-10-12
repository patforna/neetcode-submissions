class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # thoughts/ideas:
        # - recursively generate them

        if not nums:
            return [[]]

        result = self.subsets(nums[1:])
        result.extend([[nums[0]] + ss for ss in result])
        
        return result