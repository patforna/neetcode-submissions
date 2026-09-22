class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        # idea:
        # - if a and b are not same length - return early
        # - create frequency map for both a and b
        # - check if chars and frequency match

        if len(a) != len(b):
            return False

        ma, mb = {}, {}
        for c in a:
            ma[c] = ma.get(c, 0) + 1

        for c in b:
            mb[c] = mb.get(c, 0) + 1

        return ma == mb

    def isAnagram_2(self, a: str, b: str) -> bool:
        from collections import Counter

        if len(a) != len(b):
            return False

        return Counter(a) == Counter(b)