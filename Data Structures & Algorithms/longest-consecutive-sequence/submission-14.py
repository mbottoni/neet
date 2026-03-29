class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        max_seq = 0
        for n in nums:
            i = n
            if n - 1 in x:
                pass
            else:
                i = i + 1
                while i in x:
                    i = i + 1
                if max_seq < i - n:
                    max_seq = i-n
        return max_seq




        