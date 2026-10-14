class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # thoughts/ideas:
        # use a stack
        # push numbers straight onto stack
        # operators -> pop last two numbers off of stack, apply operator, put result back on stack

        def pop_two():
            return stack.pop(), stack.pop()

        stack = []
        for t in tokens:
            if t == '+':
                a, b = pop_two()
                stack.append(a + b)
            elif t == '-':
                a, b = pop_two()
                stack.append(b - a)
            elif t == '*':
                a, b = pop_two()
                stack.append(a * b)
            elif t == '/':
                a, b = pop_two()
                stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[0]
