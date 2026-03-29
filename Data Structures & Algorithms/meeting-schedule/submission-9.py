"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            for j in range(len(intervals)):
                if i!=j:
                    start2, end2 = intervals[j].start, intervals[j].end
                    if (start2 < start < end2) or (start2 < end < end2) or (start2==start and end2==end):
                        return False

        return True
