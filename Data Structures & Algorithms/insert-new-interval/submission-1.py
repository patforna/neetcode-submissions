class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:       
        result = []        
        for i in range(len(intervals)):
            cur = intervals[i]
            if new[1] < cur[0]:
                result.append(new)
                return result + intervals[i:]
            elif new[0] > cur[1]:
                result.append(cur)
            else: # overlapping case
                new = [min(new[0], cur[0]), max(new[1], cur[1])]

        result.append(new)
        return result

# intervals=[[1,2],[3,5],[9,10]], new=[6,7]        
# i=0, result=[[1,2]]
# i=1, result=[[1,2],[3,5]]
# i=2, result=[[1,2],[3,5], [6,7]] + [9,10]

# intervals=[[1,3],[4,6]], new=[2,5], result=[]

# i=0, cur=[1,3], new=[1,5], result=[]
# i=1, cur=[4,6], new=[1,6], result=[[1,6]]