class BrowserHistory:
    # thoughts/ideas:
    # - maintain a list and a pointer
    # - move pointer to go back/forward
    # - on visit, shrink list to pointer location and add new url

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        if self.current < len(self.history) - 1:
            self.history = self.history[0:self.current + 1]

        self.history.append(url)
        self.current = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]
        

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
        
# Examples:
# A, h=[A], c=0(A)
# B, h=[A,B], c=1(B)
# C, h=[A,B,C], c=2(C)
# <2, h=[A,B,C], c=0(A)
# >1, h=[A,B,C], c=1(B)
# D, h=[A,B,D], c=2(D)



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)