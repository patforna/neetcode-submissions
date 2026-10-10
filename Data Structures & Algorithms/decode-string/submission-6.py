class Solution:
    def decodeString(self, s: str) -> str:
        # thoughts/ideas:
        # - clarification: it's not just digits and letters but number and words!
        # - use a stack
        # - go through string
        #   - accumulate number or current word
        #   - on opening bracket, put (current word, number) on stack - reset number and word
        #   - on closing bracket, pop tuple from stack, multiply and append to current

        stack = []
        num, cur = 0, ""
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                cur += c
            elif c == '[':
                stack.append((cur, num))
                num, cur = 0, ""
            elif c == ']':
                prev, k = stack.pop()
                cur = prev + k * cur
        
        return cur