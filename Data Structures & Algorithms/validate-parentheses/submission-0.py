PARENS = {'(':')', '{':'}', '[':']'}

class Solution:
    def isValid(self, s: str) -> bool:
        # thoughts:
        # - use a stack
        # - open -> push
        # - close -> pop - if not maching return false
        # - return true if stack is empty

        stack = []
        for c in s:
            if c in PARENS:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                last = stack.pop()
                if PARENS[last] != c:
                    return False
        
        return len(stack) == 0
