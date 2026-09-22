class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [c.lower() for c in s if c.isalnum()] # list of alpha-numeric-only chars 

        i = 0
        j = len(l) - 1

        while i < j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1
        
        return True

        # idea

        # - two pointers - beginning, end
        # - stop when different or pointers meet