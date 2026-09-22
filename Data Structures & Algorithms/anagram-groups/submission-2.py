from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, l: List[str]) -> List[List[str]]:
        # thoughts/idea:
        # for each item:
        # - derive canonical form (i.e. frequency map)
        # - add to map, tracking canonical->[originals]
        # - convert map to list of lists
        #
        # time: n
        # space: n

        m = defaultdict(list)
        for item in l:
            k = tuple(sorted(item))
            m[k].append(item)
        
        return list(m.values())