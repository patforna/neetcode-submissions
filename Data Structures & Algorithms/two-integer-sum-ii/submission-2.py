class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # idea: 
        # - two pointers
        # - if sum < target, move left pointer (i.e. increase)
        # - otherwise move right pointer (i.e. decrease)
        # - O(n) time, O(1) space

        i = 0
        j = len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            
            if total < target:
                i += 1
            else:
                j -= 1

        raise ValueError("invalid input")