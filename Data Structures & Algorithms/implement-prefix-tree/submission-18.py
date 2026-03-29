class Node:
    def __init__(self):
        self.chars = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        cur = self.trie
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if cur.chars[index] == None:
                cur.chars[index] = Node()
                cur = cur.chars[index]
            else:
                cur = cur.chars[index]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for i in range(len(word)):
            index = ord(word[i]) - ord("a")
            if cur.chars[index] == None:
                return False
            else:
                cur = cur.chars[index]
        if cur.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if cur.chars[index] == None:
                return False
            else:
                cur = cur.chars[index]
        return True

        
        