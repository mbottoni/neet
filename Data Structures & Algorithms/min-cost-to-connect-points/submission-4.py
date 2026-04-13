class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i] = adj[i] + [[dist, j]]
                adj[j] = adj[j] + [[dist, i]]

        res = 0
        vis = set()
        min_heap = [[0,0]] # cost, point
        while len(vis)<n:
            cost, i = heapq.heappop(min_heap)
            if i in vis:
                continue
            else:
                res += cost
                vis.add(i)
                for neicost, nei in adj[i]:
                    if nei not in vis:
                        heapq.heappush(min_heap,[neicost, nei])
        return res
        