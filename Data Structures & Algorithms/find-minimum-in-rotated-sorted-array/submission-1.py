class Solution:
    def findMin(self, nums: List[int]) -> int:
        # thoughts/ideas:
        # - use a kind of binary search
        # - in a rotated array, there are two halves, which are sorted
        # - pick m, check if its l < m
        #  - if yes, the elements between l and m are sorted, i.e. l is the minimum of this half (keep track) and search the other half to see if there's a lower minimum
        #  - if not (i.e. l > m), we're looking at the portion that contains the split point (and therefore the minimum element), i.e. keep searching in this half

        result = float("inf")
        l = 0 # incl
        r = len(nums) # excl
        while l < r:
            m = l + (r - l) // 2
            if nums[l] < nums[m]:
                result = min(result, nums[l])
                l = m + 1
            else:
                result = min(result, nums[m])
                r = m

        return result
#
# nums=[4,5,0,1,2,3]
#       0 1 2 3 4 5 

# l=0, r=6, m=3, nums[m]=1, result=[1]
# l=0, r=3, m=1, nums[m]=5, result=[1]
# l=2, r=3, 




