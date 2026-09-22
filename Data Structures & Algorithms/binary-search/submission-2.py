class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # idea - binary search:
        # - select middle element
        # - if equal to target -> done
        # - if < target -> repeat search in left half (recursively or iteratively by updaint boundary conditions - we'll do the latter)
        # - if > target -> search right half

        l = 0 # inclusive
        r = len(nums) # exclusive
        while l < r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m
            else:
                l = m + 1
        
        return -1

# -1,0,3,5,9,12, target=9
#  0 1 2 3 4 5
# len=6
 
# l=0, r=6, m=3, nums[m]=5
# l=4, r=6, m=1, nums[m]=5
