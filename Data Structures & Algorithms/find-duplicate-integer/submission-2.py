class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = set()
        for n in nums:
            if n in h:
                return n
            else:
                h.add(n)
        return -1
        