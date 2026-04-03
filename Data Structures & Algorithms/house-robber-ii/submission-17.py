class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        ar = [None] * n

        def dfs(nums, i):
            if i > len(nums) - 1:
                return 0
            elif ar[i] is not None:
                return ar[i]
            else:
                ar[i] = max(nums[i] + dfs(nums, i+2), dfs(nums, i+1))
                return ar[i]

        res1 = dfs(nums[1:], 0)
        ar[:] = [None] * n  # reset cache
        res2 = dfs(nums[:-1], 0)
        return max(res1, res2)