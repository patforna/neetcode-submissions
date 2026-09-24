from collections import defaultdict

# thoughts/ideas:
# use a dict underneath. keys: str, value: [(timestamp, value)]
# values will be sorted by timestamp automatically because setting is strictly increasing
# on get, find value with matching or closest previous timestamp using binary search - O(log t) - number of timestamps

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        result = ""
        entries = self.d[key]
        l = 0 #incl
        r = len(entries) #excl
        while l < r:
            m = l + (r - l) // 2
            ts, val = entries[m]
            if ts == timestamp:
                return val
            if ts < timestamp:
                result = val
                l = m + 1
            else:
                r = m

        return result

# d["key1"]=[(10, "value1"), (3, "sad")]