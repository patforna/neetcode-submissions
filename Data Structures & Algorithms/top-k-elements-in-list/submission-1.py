from collections import defaultdict

class Solution:
    def topKFrequent(self, l: List[int], k: int) -> List[int]:
        
        frequencies = defaultdict(int)
        for it in l: # O(n)
            frequencies[it] += 1        

        # +1 so we don't need to zero-base frequency access
        buckets = [[] for _ in range(len(l) + 1)] # O(n), space: O(n)
        for it, fr in frequencies.items(): # O(n)
            buckets[fr].append(it) # O(1)

        result = []
        for i in range(len(buckets) - 1, 0, -1): # O(n)
            for it in buckets[i]:
                result.append(it)
            if len(result) == k:
                return result
                
        raise RuntimeError("should never get here")
