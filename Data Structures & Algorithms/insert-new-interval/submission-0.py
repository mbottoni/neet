class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            if newInterval[0] > end:
                res.append([start, end])
                i += 1
            elif newInterval[1] < start:  # new interval is fully before current
                break
            else:
                newInterval[0] = min(start, newInterval[0])  # fixed variable names
                newInterval[1] = max(end, newInterval[1])    # fixed variable names
                i += 1

        res.append(newInterval)  # add the (possibly merged) new interval

        while i < len(intervals):  # add remaining intervals
            res.append(intervals[i])
            i += 1

        return res