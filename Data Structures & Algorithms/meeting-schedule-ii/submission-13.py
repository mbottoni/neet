"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        m_rooms=1
        if len(intervals)==0:
            return 0
        for i in range(len(intervals)):
            rooms = 1
            for j in range(len(intervals)):
                if i != j:
                    start, end   = intervals[i].start, intervals[i].end
                    start2, end2 = intervals[j].start, intervals[j].end
                    if (start==end and start2==end2) or (start2<start<end2):
                        rooms += 1
                        m_rooms = max(rooms, m_rooms)

        return m_rooms

        