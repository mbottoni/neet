from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def run(nums):
            if len(nums) == 0:
                return 0
                
            best = 0
            for i in range(len(nums)):
                if i == 0:
                    c = 1 * nums[i] * (nums[i+1] if len(nums) > 1 else 1)
                    best = max(best, c + run(nums[1:]))
                elif i == len(nums)-1:
                    c = nums[i-1] * nums[i] * 1
                    best = max(best, c + run(nums[:-1]))
                else:
                    c = nums[i-1] * nums[i] * nums[i+1]
                    best = max(best, c + run(nums[:i] + nums[i+1:]))
            return best

        return run(tuple(nums))