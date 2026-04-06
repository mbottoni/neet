from math import prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        min_prod = 1
        res = max(nums)

        for n in nums:
            if n == 0 :
                max_prod, min_prod = 1, 1
            else:
                tmp = max_prod
                max_prod = max(n * max_prod, n * min_prod, n)
                min_prod = min(n * tmp, n * min_prod, n)
                res = max(res, max_prod)

        return res





        