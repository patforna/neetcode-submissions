class Solution:
    def threeSum(self, l: List[int]) -> List[List[int]]:
        # all triplets that sum up to zero - all distinct indices
        #
        # if we knew all pairs, it would be 2sum (just find complement)
        #
        # complexity? O(n^2) time, O(1) space
        #
        # brute force -> 3 pointers -> O(n^3)
        #
        # O(n^2) solution
        # - sort
        # - one pointer going from left to right
        # - inner loop with two pointers starting at next/last element
        # - finding complement sum.
        # - if too small, advance left inner pointer
        # - if too large, advance (from right to left) right inner pointer
        # - if complement found, add to results list
        # - keep going until left inner pointer == right inner pointer

        l.sort()  # O(n log n)
        result = []
        for i in range(len(l) - 2):  # O(n^2)
            if i > 0 and l[i] == l[i - 1]:
                continue

            j = i + 1
            k = len(l) - 1
            while j < k:
                total = l[i] + l[j] +l[k]
                if total == 0:
                    result.append([l[i], l[j], l[k]])
                    j += 1
                    k -= 1
                    # move pointer to skip duplicates
                    while j < k and l[j] == l[j - 1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
