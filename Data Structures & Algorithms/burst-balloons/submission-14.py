from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad with boundary 1s
        nums = [1] + nums + [1]
        n = len(nums)

        @cache
        def dp(left, right):
            if right - left < 2:  # no balloons between boundaries
                return 0
            
            best = 0
            for k in range(left + 1, right):  # k is the LAST balloon burst in (left, right)
                coins = nums[left] * nums[k] * nums[right]
                best = max(best, coins + dp(left, k) + dp(k, right))
            return best

        return dp(0, n - 1)