class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # thoughts/ideas:
        #
        # - problem doesn't say they're sorted - assumption: not sorted
        #
        # - sort the intervals by start time - O(n log n) time
        # - do one pass through the sorted list: O(n) time
        #   - if start time of next interval <= end time of current interval -> merge next into current
        #   - else, add current to result list - O(n) space
        # Overall: O(n log n) time, O(n) space

        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        
        result = []
        last = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= last[1]:
                last[1] = max(cur[1], last[1])
            else:
                result.append(last)
                last = cur

        result.append(last)
        
        return result
        