from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # thoughts/ideas:
        # - sliding window - expand to right, shrink left - O(n)
        # - maintain frequency map of chars inside window

        if t == "":
            return ""

        res = [-1, -1]
        res_len = float("inf")

        window = defaultdict(int)
        count_t = dict(Counter(t))

        have, need = 0, len(count_t)
        l = 0
        for i, c in enumerate(s):
            window[c] += 1

            if c in count_t and window[c] == count_t[c]:
                have += 1

                while have == need:
                    if (i - l + 1) <= res_len:
                        res = [l, i]
                        res_len = i - l + 1

                    # pop from left of window 
                    window[s[l]] -= 1
                    if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                        have -= 1
                    
                    l += 1

        return s[res[0]:res[1] + 1] if res_len < float("inf") else ""