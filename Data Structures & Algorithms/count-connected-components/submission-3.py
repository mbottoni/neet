class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        n_connected = 0
        # Construct adj matrix
        from collections import defaultdict
        d=defaultdict(list)
        for nx,ny in edges:
            d[nx] = d[nx] + [ny]
            d[ny] = d[ny] + [nx]

        visited = set()
        
        def visit_all_nodes(node):
            if node in visited:
                return
            nei = d[node]
            visited.add(node)
            for n in nei:
                visit_all_nodes(n)

        for i in range(n):
            if i in visited:
                pass
            else:
                visit_all_nodes(i)
                n_connected += 1

        return n_connected
        