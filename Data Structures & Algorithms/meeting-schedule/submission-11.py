"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meets = []
        for i in range(len(intervals)):
            meets.append([intervals[i].start, intervals[i].end])
        meets = sorted(meets, key=lambda item: item[0]) # Sort by start date
        print(meets)
        for i in range(len(meets)-1):
            if meets[i][1] > meets[i+1][0]:
                # the end of the current meeting is greater than the start of the next
                return False

        return True
