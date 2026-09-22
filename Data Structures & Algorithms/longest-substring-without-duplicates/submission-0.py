class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force solution:
        #
        # start checking at every possible starting point -> O(n^2)
        # 
        # different idea:

        # better approach: sliding window -> O(n)
        # expand window, until we find a duplicate
        # while expanding window:
        #     keep track of global max window size
        #     keep track of seen elements in a hash map for constant time dupe detection
        # when a duplicate was found
        #     shrink left window edge to drop duplicate from window
        #     also drop all items that fell out of window from dupe hash map

        max_window = 0
        l, i = 0, 0 # left (incl), right/current (incl)
        d = {} # chars-to-index in current substring

        while i < len(s):
            c = s[i]
            if c not in d:
                max_window = max(max_window, i - l + 1)                
            else:                
                # drop all elements leading up to c incl. c, while shrinking left side of window
                last = d[c]
                while l <= last:
                    del d[s[l]]
                    l += 1
            
            d[c] = i # remember current char for dupe detection
            i += 1

        return max_window
