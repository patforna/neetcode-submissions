OPERATORS = {'+', '-', '/', '*'}

class Solution:
    def calculate(self, s: str) -> int:
        # thoughts/ideas:
        # - operator precedence, e.g. 3 + 5 / 2 => division before addition
        # - could build an expression tree and do a tree traversal        
        # - or a stack, if i add "invisible parens"? e.g. (3 * 2) + 5 = [5, 5]
        # - either way, maybe first tokenise? [3, *, 2, +, 5]
        #
        # - stack is probably simpler
        # - operator precedence can be handled in the following way:
        #   - + and - will be deferred, i.e. we push the numbers onto the stack (negate for substraction)
        #   - * and / will be computed directly by taking the current number and * or / with what's on top of the stack
        #     then we replace what's on top
        # - at the end, we sum everything together.

        tokens = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in OPERATORS:
                tokens.append(num)
                tokens.append(c)
                num = 0
            # else ignore/skip

        tokens.append(num) 

        print(tokens)
        stack = []
        last_op = '+'
        for i in range(len(tokens)):
            if tokens[i] in OPERATORS:
                last_op = tokens[i]
                continue

            num = tokens[i]
            match last_op:
                case '+':
                    stack.append(num)
                case '-':
                    stack.append(-num)
                case '*':
                    stack.append(stack.pop() * num)
                case '/':
                    stack.append(int(stack.pop() / num))
            # print(f"after: num={num}, stack={stack}")

        result = 0
        while stack:
            result += stack.pop()

        return result

3+2*2

            


        