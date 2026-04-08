class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n + 1) * n // 2
        total_sum = sum(nums)
        return expected_sum - total_sum
        