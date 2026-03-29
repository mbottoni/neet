class Node:
    def __init__(self):
        self.chars = [None] * 27
        self.end = False

class WordDictionary:
    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for i in range(len(word)):
            # Keep your original index logic
            index = 26 if word[i] == '.' else ord(word[i]) - ord('a')
            
            if cur.chars[index] is None:
                cur.chars[index] = Node()
                
            cur = cur.chars[index]
        cur.end = True

    def search(self, word: str) -> bool:
        # We need a helper to handle the branching logic of the '.' wildcard
        def dfs(idx, node):
            cur = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    # Check every possible single-char branch at this position
                    for child in cur.chars:
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False
                
                index = ord(char) - ord('a')
                if cur.chars[index] is not None:
                    cur = cur.chars[index]
                else:
                    return False
            return cur.end

        return dfs(0, self.trie)