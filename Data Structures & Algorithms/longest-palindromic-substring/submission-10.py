class Solution:
    def longestPalindrome(self, s: str) -> str:
        # thoughts/ideas:
        # - for each character, try expanding "outwards" on both sides O(n^2)
        # - maintina max_length

        longest = ""
        for i in range(len(s)):
            
            # uneven length
            for j in range(len(s)):
                l = i - j # inclusive
                r = i + j # inclusive
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break
                if r + 1 - l > len(longest):
                    longest = s[l:r + 1]

            # even length
            for j in range(len(s)):
                l = i - j # inclusive
                r = i + j + 1 # inclusive
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break
                if r + 1 - l > len(longest):
                    longest = s[l:r + 1]
        
        return longest

# s="abbc"
# l=a
# i=0, l=a
# i=1, j