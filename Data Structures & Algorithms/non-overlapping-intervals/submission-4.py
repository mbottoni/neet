class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda item: item[0]) # 

        n_count = 0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            curr_start = intervals[i][0]

            if prev_end > curr_start:
                n_count += 1
                prev_end = min(intervals[i][1], prev_end)
            else:
                prev_end = intervals[i][1]


        return n_count
        