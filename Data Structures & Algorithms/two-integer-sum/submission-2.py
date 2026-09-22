class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        # thoughts / ideas:
        #
        # - loop through n
        #   - maintain hash map of numbers seen
        # .  - if complement is found in hash map, return

        m = {}
        for i, v in enumerate(n):
            compl = t - v
            if compl in m:
                return [m[compl], i]

            m[v] = i

        return []
