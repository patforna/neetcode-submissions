class Solution:
    def search(self, a: List[int], target: int) -> int:
        # thoughts/ideas:
        # 
        # - in a rotated array, there are two halves, which are sorted
        # - if a[l] < a[m], we are in a sorted half:
        #   - if a[l] <= target <= a[m], do a normal binary search in this half
        #   - else, search in other half
        # - otherwise, we are spanning two halves:
        #   - if a[l] <= target, keep searching in this half (because the other half won't contain elements greater than a[l])
        #   - else, search in other half

        l = 0 # incl
        r = len(a) # excl
        while l < r:
            m = l + (r - l) // 2
            if target == a[m]:
                return m
            if a[l] <= a[m]: # inside sorted half
                if a[l] <= target and target < a[m]:
                    r = m
                else:
                    l = m + 1
            else: # spanning split (i.e. contains min an max elements)
                if a[l] <= target or target <= a[m]:
                    r = m
                else:
                    l = m + 1

        return -1


# a=[5,1,2,3,4], target=1
#    0 1 2 3 4

# l=0, r=5, m=2, a[m]=2
