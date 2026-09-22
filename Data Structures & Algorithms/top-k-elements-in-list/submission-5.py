from collections import Counter
import heapq

class Solution:
    def topKFrequent_(self, nums: List[int], k: int) -> List[int]:
        # idea #1
        # 
        # - create frequency map - O(n) time and space
        # - pour frequencies into buckets, where buckets[count] = [numbers]
        # - walk buckets from back, pulling out k numbers

        counter = Counter(nums)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items(): # key = number, val = frequency
            buckets[freq].append(num)

        result = []
        for bucket in reversed(buckets):
            result.extend(bucket)
            if len(result) >= k:
                break
        
        return result[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea #2
        # 
        # - calculate frequencies O(n)
        # - create min heap of size k - O(n log k) from frequencies
        # - return items (unsorted)

        counter = Counter(nums)

        # (1,1), (2, 2), (3, 3)

        heap = []
        for num, freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))

        return [num for _, num in heap] # any order, which is OK according to problem statement









