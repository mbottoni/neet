import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean(x,y):
            x1,y1 = x
            x2,y2 = y
            return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

        d={}
        for i in range(len(points)):
            distance = euclidean(points[i], [0,0])
            d[i] = distance

        d = {k:v for k,v in sorted(d.items(), key=lambda item: item[1])}
        k_closest = list(d.keys())[:k]
        ans = []
        for i in k_closest:
            ans.append(points[i])
        return ans
        

        