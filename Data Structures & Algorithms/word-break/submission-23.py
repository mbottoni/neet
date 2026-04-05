class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cond = []
        def dfs(st):
            if st == "#" * len(s):
                cond.append(True)
            else:
                for word in wordDict:
                    if word in st:
                        dfs(st.replace(word, "#" * len(word)))

        dfs(s)
        return any(cond)
