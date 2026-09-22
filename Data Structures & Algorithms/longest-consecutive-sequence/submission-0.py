class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # idea: 
        # - find starting elements - O(n) space and time
        #   - create set - O(n) space and time
        #   - for each element, check if num-1 is in the set - O(n) time
        # - for each starting element, count consecutive length - O(n) time (because no overlap possible)
        #   - keep track of longest

        nums_set = set(nums)
        beginnings = [num for num in nums if num - 1 not in nums_set]

        longest = 0
        for beginning in beginnings:
            length = 0
            num = beginning
            while num in nums_set:
                length += 1
                num += 1
            longest = max(longest, length)

        return longest

# nums_set: 1, 2, 3, 10, 11, 12  
# beginnings: 1, 10

# beginning=1
#   num = 1, length=1
#   num = 2, length=2
#   num = 3, length=3
#   longest = 3