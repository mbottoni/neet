class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_soma = nums[0]
        current = nums[0]
        
        for num in nums[1:]:
            current = max(num, current + num)
            max_soma = max(max_soma, current)
        
        return max_soma