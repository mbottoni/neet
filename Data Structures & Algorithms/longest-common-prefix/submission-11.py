class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        l=""

        while True:
            chars = []
            for i in range(len(strs)):
                st = strs[i]
                if len(st)==0:
                    return ""

                if len(st)>0 and pointer < len(st):
                    chars.append(st[pointer])
                else:
                    break

            if len(chars) == len(strs) and len(set(chars)) == 1:
                l = l + chars[0]
                pointer += 1
            else:
                return l

        return l

        