class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, cur = nums[0], 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur+=n
            maxi = max(maxi, cur)

        return maxi