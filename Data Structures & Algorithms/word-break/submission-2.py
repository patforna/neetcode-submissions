from functools import cache

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:

        @cache
        def _wordbreak(i):
            if i >= len(s):
                return True

            for word in words:
                if s[i:].startswith(word) and _wordbreak(i + len(word)):
                    return True

            return False

        return _wordbreak(0)

        