class Solution:
    def search(self, a: List[int], t: int) -> int:
        # Idea:
        # Binary Search
        # Find the midpoint m.
        # Check if a[l] <= a[m]. If it is, the left half is perfectly sorted.
        # If the target falls cleanly within the boundaries of that sorted left half, narrow search to the left (r = m - 1).
        # Otherwise, the target must be in the un-sorted right half (l = m + 1).
        # If the left half isn't sorted, it means the right half must be perfectly sorted.
        # If the target falls cleanly within the sorted right half (a[m] < t <= a[r]), narrow your search to the right (l = m + 1).
        # Otherwise, search the left half (r = m - 1).

        l = 0 # incl
        r = len(a) # excl        

        while l < r:
            m = l + (r - l) // 2

            if a[m] == t:
                return m

            if a[l] <= a[m]: # left half is sorted
                if a[l] <= t < a[m]: # target is in this half
                    r = m
                else: # target is in other half
                    l = m + 1
            
            else: # right half is sorted
                if a[m] < t <= a[r - 1]: # target is in this half
                    l = m + 1
                else: # target is in the other half
                    r = m
        
        return -1