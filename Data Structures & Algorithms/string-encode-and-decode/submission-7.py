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
                while j < len(s) and s[j] != delimiter: 
                    n = n + s[j]
                    j += 1
                number_of_chars = int(n)
                word = s[j+1 : j+1+number_of_chars]
                decoded.append(word)
                i = j + 1 + number_of_chars         
            else:
                i += 1
    
        return decoded
    