from math import prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -float('inf')
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod = prod * nums[j]
                max_prod = max(max_prod, prod)

        return max_prod



        