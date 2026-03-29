from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key] = self.d[key] + [[timestamp, value]]
        self.d = defaultdict(list, {k: v for k, v in sorted(self.d.items(), key=lambda item: item[1][0])})

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid-1
        if len(arr)==0 or arr[0][0]>timestamp:
            return ""
        return arr[right][1]
        
