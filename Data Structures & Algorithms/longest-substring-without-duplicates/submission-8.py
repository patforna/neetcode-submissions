class Solution:
    def lengthOfLongestSubstring_(self, s: str) -> int:
        # thoughts
        # - sliding window problem
        # - two pointers, variable length O(n) time
        # - keep set of current window elemens - O(k) space (where k longest substring; k <= n)
        # - keep track of longest

        i = 0
        j = 0
        seen = set()
        longest = 0
        while j < len(s):
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                longest = max(longest, len(seen))
                j += 1
            
            # short-circuit - can only get shorter from here
            if j == len(s): 
                break

            # move left pointer past initial duplicate
            while i < j:
                removed = s[i]
                seen.remove(s[i])
                i += 1
                if removed == s[j]:
                    break

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        i = 0
        for j, c in enumerate(s):
            c = s[j]
            while c in seen:
                seen.remove(s[i])
                i += 1

            seen.add(c)
            longest = max(longest, j - i + 1)
        
        return longest

# "dvdf"
#  0123
# len(s)=4

# i=0, j=0, s[i]='d', s[j]='d', seen={'d'}, longest=1
# i=0, j=1, s[i]='d', s[j]='v', seen={'d', 'v'}, longest=2
# i=0, j=2, s[i]='d', s[j]='d', seen={'d', 'v'}, longest=2
# i=1, j=2, s[i]='d', s[j]='d', seen={'v'}, longest=2



