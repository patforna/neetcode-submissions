from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # thoughts/ideas:
        # - two pointers, sliding window with variable length
        # - compute frequency map 
        # - compute most frequent char (mfc) in the window - O(26)
        # - if diff between mfc and window size is <= k, expand window (right + 1)
        # - otherwise shrink window (left + 1) and update frequency map

        i = 0
        longest = 0
        counts = defaultdict(int)
        for j, c in enumerate(s):
            counts[c] += 1
            if j + 1 - i - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1
            else:
                longest = max(longest, j + 1 - i)

        return longest