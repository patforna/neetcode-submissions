class MinStack:
    # thoughts/ideas:
    # - all except min are trivially supported by a list already
    # - to support min, add a tuple of (val, min) at each level

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        mn = val if not self.stack else min(val, self.getMin())
        self.stack.append((val, mn))
        
    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int | None:
        return self._top()[0]

    def getMin(self) -> int | None:
        return self._top()[1]

    def _top(self) -> Tuple[int, int]:
        if not self.stack:
            return None
        return self.stack[-1]
        
