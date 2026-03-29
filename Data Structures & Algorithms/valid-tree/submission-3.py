class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        d = defaultdict(list)
        for nx, ny in edges:
            d[nx] = d[nx] + [ny]
            d[ny] = d[ny] + [nx]

        # Count components
        visited = set()
        def visit_nodes(i):
            if i in visited:
                return
            visited.add(i)
            for neighbor in d[i]:
                visit_nodes(neighbor)

        num_comp = 0
        for i in range(n):
            if i not in visited:
                visit_nodes(i)
                num_comp += 1

        # Check for cycle
        def check_cy(node, parent):
            if node in visited:
                cond.append(False)
                return
            else:
                visited.add(node)
                nei = d[node]
                for n in nei:
                    if n != parent:
                        check_cy(n, node)

        visited = set()
        cond = []
        check_cy(0, -1)
        if cond:
            return False

        return num_comp == 1