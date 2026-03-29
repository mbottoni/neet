class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)
        n = len(edges)  # FIX 1: nodes are 1..n, so n = len(edges), not len(edges)-1
        for nx, ny in edges:
            d[nx] = d[nx]+[ny]
            d[ny] = d[ny]+[nx]

        def remove_edge(d, edge):
            nx, ny = edge
            e_nx = d[nx][:]
            e_ny = d[ny][:]
            print(e_nx)

            e_nx.remove(ny)   # FIX 3: remove the neighbor, not self
            e_ny.remove(nx)

            new_d = defaultdict(list, d)  # FIX 4: don't mutate original d
            new_d[nx] = e_nx
            new_d[ny] = e_ny

            return new_d

        def check_componnent(new_d):
            visited = set()
            def visit_nodes(i):
                if i in visited:
                    return
                else:
                    visited.add(i)
                    nei = new_d[i]  # FIX 5: use new_d, not outer d
                    for n in nei:
                        visit_nodes(n)
            num = 0
            for i in range(1, n+1):  # FIX 6: nodes are 1-indexed
                if i not in visited:
                    visit_nodes(i)
                    num+=1
            return num

        possibles = []
        for edge in edges:
            new_d = remove_edge(d, edge)
            num = check_componnent(new_d)
            if num==1:
                possibles.append(edge)

        return possibles[-1]