class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # thoughts/ideas:
        # - use a stack
        # - push elements that are smaller
        # - invariant: stack will be in monotonically decreasing order

        stack = []
        result = [0] * len(temps)
        for i, t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            
            stack.append(i)
        
        return result

# temps  = [6,7,8,4,2,3,5]
# result = [0,0,0,0,0,0,0]
#           0 1 2 3 4 5 6

# i=0, t=6, s=[0(6)]
# i=1, t=7, s=[1(7)], j=0, [1,0,0,0,0,0,0]
# i=2, t=8, s=[2(8)], j=1, [1,1,0,0,0,0,0]
# i=3, t=4, s=[2(8),3(4)]
# i=4, t=2, s=[2(8),3(4),4(2)]
# i=5, t=3, s=[2(8),3(4),5(3)], j=4, [1,1,0,0,1,0,0]
# i=6, t=5, s=[2(8)], j=, [1,1,0,3,1,1,0]