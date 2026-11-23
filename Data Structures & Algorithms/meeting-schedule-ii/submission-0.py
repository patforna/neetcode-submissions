"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:    
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # thoughts / ideas:
        # - assumption: intervals are not already sorted
        # - find max number of overlapping meetings
        #   - get all start times (sorted)
        #   - get all end times (sorted)
        #   - use two pointers and maintain a counter
        #   - if a meeting starts before another one ends, increment counter and move pointer
        #   - return max counter value

        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])

        i, j, count, max_count = 0, 0, 0, 0

        while i < len(starts):
            if starts[i] < ends[j]:
                count += 1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                j += 1
        
        return max_count

# Input: intervals = [(0,40),(5,10),(15,20)]

# starts = [0,5,15]
# ends = [10,20,40]

# i=0, j=0, s[i]=0,  e[j]=40, c=1, mc=1
# i=1, j=0, s[i]=5,  e[j]=10, c=2, mc=2
# i=2, j=0, s[i]=15, e[j]=10, c=1, mc=2
# i=2, j=1, s[i]=15, e[j]=20, c=2, mc=2
        