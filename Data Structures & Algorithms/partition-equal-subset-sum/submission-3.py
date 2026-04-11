class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = {0}
        for n in nums:
            for possible_sum in dp.copy():
                dp.add(possible_sum + n)

        return target in dp