class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        delimiter = "#"
        for s in strs:
            n = str(len(s))
            encoded = encoded + delimiter + n + delimiter + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        delimiter = "#"
        i = 0
        while i < len(s):
            if s[i] == delimiter:
                j = i + 1
                n = ""
                while j < len(s) and s[j] != delimiter:  # Fix 1: compare s[j], not j
                    n = n + s[j]
                    j += 1
                number_of_chars = int(n)
                word = s[j+1 : j+1+number_of_chars]      # Fix 2: correct slice end
                decoded.append(word)
                i = j + 1 + number_of_chars               # Fix 3: correct next position
            else:
                i += 1
    
        return decoded
    