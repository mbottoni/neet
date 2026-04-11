import heapq
class MedianFinder:
    def __init__(self):
        self.n = 0
        self.arr = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr, num)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            x = heapq.nsmallest(1 + self.n // 2, self.arr)  # fix 1 & 2
            return (x[-1] + x[-2]) / 2
        else:
            return heapq.nsmallest(self.n // 2 + 1, self.arr)[-1]  # fix 3