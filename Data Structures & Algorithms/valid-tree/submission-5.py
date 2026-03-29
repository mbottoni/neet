class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        from collections import defaultdict
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in d[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited) == n