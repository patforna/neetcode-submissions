from collections import defaultdict

class Solution:
    def groupAnagrams(self, l: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in l:
            k = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                k[i] += 1

            m[tuple(k)].append(s)

        return list(m.values())