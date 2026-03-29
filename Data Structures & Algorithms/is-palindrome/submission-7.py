class Solution:
    def isPalindrome(self, s: str) -> bool:
        cond = []
        s = [c for c in s if c.isalnum()]
        print(s)
        for i in range(len(s)):
            if s[-i-1].lower() == s[i].lower():
                cond.append(True)
            else:
                cond.append(False)

        print(cond)
        return all(cond)
        