class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def dist(s1, s2):
            dist = 0
            for i in range(min(len(s2), len(s1))):
                if s1[i] != s2[i]:
                    dist += 1
            return dist + abs(len(s2) - len(s1))

        wordSet = set(wordList)
        q = deque([(beginWord, 1)])
        vis = set()
        vis.add(beginWord)

        while q:
            word, count = q.popleft()
            if endWord==word:
                return count
            for w in wordList:
                d = dist(w, word)
                if w not in vis and d==1:
                    vis.add(w)
                    q.append((w,count+1))
        

        return 0