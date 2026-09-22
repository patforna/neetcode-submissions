class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) # incl, excl.

        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1            
            else:
                return mid
            
        return -1
