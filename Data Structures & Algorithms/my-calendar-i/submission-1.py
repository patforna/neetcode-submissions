class MyCalendar:
    # thoughts/ideas:
    # - maintain list of existing meetings
    # - when booking a new meeting, go through existing meetings
    #   and make sure none overlap - O(n) time but de facto constant because n < 1000    
    def __init__(self):
        self.events = []    

    def book(self, start: int, end: int) -> bool:
        for ex_start, ex_end in self.events:
            # overlaps on existing start time
            if start < ex_start and end > ex_start:
                return False
            # overlaps inside existing event
            if start >= ex_start and end <= ex_end:
                return False
            # overlaps on existing end time
            if start < ex_end and end > ex_end:
                return False

        self.events.append((start, end))
        return True

# Examples:
# events=[(3,5)]
# 1,2 - True
# 1,3 - True
# 1,4 - False
# 1,5 - False
# 1,6 - False
# 3,4 - False
# 3,5 - False
# 3,6 - False
# 5,6 - True
# 6,7 - True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)