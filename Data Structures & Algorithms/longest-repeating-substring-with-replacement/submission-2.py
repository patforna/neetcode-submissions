from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # thoughts/ideas:
        # - two pointers, sliding window with variable length
        # - compute frequency map 
        # - compute most frequent char (mfc) in the window - O(26)
        # - if diff between mfc and window size is <= k, expand window (right + 1)
        # - otherwise shrink window (left + 1) and update frequency map

        # j = k + 1
        i = 0 #incl
        j = 0 #incl
        longest = 0
        counts = defaultdict(int)
        for j, c in enumerate(s):
            counts[c] = counts[c] + 1

            if j + 1 - i - max(counts.values()) > k:
                counts[s[i]] = counts[s[i]] - 1
                i += 1
            else:
                longest = max(longest, j + 1 - i)

        return longest

# AAABABB  k=1
# 0123456

# i=0, j=0, counts={A:1}, longest=1
# i=0, j=1, counts={A:2}, longest=2
# i=0, j=2, counts={A:3}, longest=3
# i=0, j=3, counts={A:3,B:1}, longest=4
# i=0, j=4, counts={A:4,B:1}, longest=5
# i=1, j=5, counts={A:3,B:2}, longest=5
# i=1, j=6, counts={A:3,B:3}, longest=5