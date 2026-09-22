from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea #1
        # 
        # - create frequency map - O(n) time and space
        # - pour frequencies into buckets, where buckets[count] = [numbers]
        # - walk buckets from back, pulling out k numbers

        counter = Counter(nums)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in counter.items(): # key = number, val = frequency
            buckets[val].append(key)

        result = []
        for bucket in reversed(buckets):
            result.extend(bucket)
            if len(result) >= k:
                break
        
        return result[:k]