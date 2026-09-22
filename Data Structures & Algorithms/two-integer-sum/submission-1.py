class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        m = {x:i for i, x in enumerate(n)}
        for i, x in enumerate(n):
            j = m.get(t - x, False)
            if j and i != j:
                return [i, j]
        
        raise ValueError()


