class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        ma, mb = {}, {}
        for x in a:
            ma[x] = ma.get(x, 0) + 1
        
        for x in b:
            mb[x] = mb.get(x, 0) + 1

        for k in ma:
            if k not in mb or mb[k] != ma[k]:
                return False

        return True