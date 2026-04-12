from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def run(index, soma):
            # out of bound
            if index == len(nums):
                return 1 if soma == target else 0
            # reach target
            return run(index+1, soma-nums[index])+run(index+1, soma+nums[index])

        return run(0, 0)


