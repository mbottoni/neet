class Node:
    def __init__(self):
        self.vis = [None] * 26
        self.endofword = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
            dummy = Node()
            for word in words:
                node = dummy
                for c in word:
                    index = ord(c) - ord('a')
                    if node.vis[index] is None:          # only create if missing
                        node.vis[index] = Node()
                    node = node.vis[index]
                node.endofword = True
            return dummy

        def dfs(i, j, node, path, visited):
            if node.endofword:
                res.append(path)
                node.endofword = False                   # avoid duplicates
            
            for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                ni,nj = i+di,j+dj
                if ni >=0 and ni<len(board) and nj>=0 and nj<len(board[0]):
                    c = board[ni][nj]
                    index = ord(c)-ord('a')
                    if node.vis[index] and (ni,nj) not in visited:
                        visited.add((ni,nj))
                        dfs(ni,nj,node.vis[index],path+c,visited)
                        visited.remove((ni,nj))



        trie = build_trie(words)
        res = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                index = ord(c) - ord('a')
                if trie.vis[index] is not None:
                    dfs(i, j, trie.vis[index], c, {(i, j)})

        return res