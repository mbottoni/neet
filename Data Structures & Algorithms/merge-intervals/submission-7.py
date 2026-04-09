class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        res = []
        intervals = sorted(intervals, key=lambda item:item[0])

        s = intervals[0][0]
        e = intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] <= e:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
            else:
                res.append([s, e])
                s, e = intervals[i][0], intervals[i][1]  # fix: reset s and e

            i += 1

        res.append([s, e])  # fix: append the last interval
        return res