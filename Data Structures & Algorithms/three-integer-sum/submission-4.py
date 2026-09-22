class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # thoughts/ideas:
        # - sort nums - n log n, in-place
        # - then, go through each element and find TwoSum II - O(n^2)

        nums.sort()  # in-place
        result = []
        for ia in range(len(nums) - 2):
            if ia > 0 and nums[ia] == nums[ia - 1]:  # skip duplicate a values
                continue

            # TwoSum II
            ib = ia + 1
            ic = len(nums) - 1
            while ib < ic:
                if ib > ia + 1 and nums[ib] == nums[ib - 1]:  # skip duplicate b values
                    ib += 1
                    continue

                total = nums[ia] + nums[ib] + nums[ic]
                if total == 0:                    
                    result.append([nums[ia], nums[ib], nums[ic]])
                    ib += 1
                    ic -= 1
                elif total < 0:
                    ib += 1
                else:
                    ic -= 1

        return result


# nums = [-1, -2, -2, 3, 3]
# [-1, -2, 3]
