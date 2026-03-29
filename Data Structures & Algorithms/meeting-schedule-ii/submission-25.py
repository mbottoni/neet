"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # heap solution
        h = [] # this will be a min heap storing the end time of the meeting

        meets = []
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            meets.append([start,end])
        meets =sorted(meets, key = lambda item : item[0]) # O(nlogn)

        
        m_size = 0
        for i in range(len(meets)):
            if len(h) > 0 and h[0] <= meets[i][0]:
                heapq.heappop(h)
            heapq.heappush(h, meets[i][1])
            m_size = max(m_size, len(h))

        return m_size

        

        