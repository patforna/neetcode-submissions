class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # thoughts/ideas:
        # - scan from left to right, maintaining current min/max of subarray up to that point

        res = max(nums)
        cur_min, cur_max = 1, 1
        
        for n in nums:
          if n == 0:
            cur_min, cur_max = 1, 1
            continue

          old_min = cur_min
          cur_min = min(n, old_min * n, cur_max * n)
          cur_max = max(n, old_min * n, cur_max * n)
          
          res = max(cur_max, res)

        return res