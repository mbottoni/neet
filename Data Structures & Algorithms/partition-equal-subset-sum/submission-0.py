class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = {0}
        for n in nums:
            dp = {s + n for s in dp} | dp

        return target in dp