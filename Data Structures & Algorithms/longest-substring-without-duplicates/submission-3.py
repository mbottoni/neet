class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        i = 0 
        max_len = 0
        saw = set()


        while i < n and j < n:
            if s[j] in saw:
                saw.remove(s[i])
                i += 1
            elif s[j] not in saw:
                saw.add(s[j])
                j+=1

            max_len = max(j - i,max_len)

        return max_len







        