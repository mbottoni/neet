class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def dist(s1, s2):
            dist = 0
            for i in range(min(len(s2), len(s1))):
                if s1[i] != s2[i]:
                    dist += 1
            return dist + abs(len(s2) - len(s1))

        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        vis = {beginWord}

        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            for w in wordList:
                if dist(word, w) == 1 and w not in vis:
                    vis.add(w)
                    queue.append((w, count + 1))

        return 0