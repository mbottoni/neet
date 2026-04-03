class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ar = [None] * n
        def dfs(i):
            if i > n-1:
                return 0
            elif ar[i]!=None:
                # max amount of money until house i
                return ar[i]
            else:
                ar[i] = max(dfs(i+1), nums[i] + dfs(i+2))
                return ar[i]

        return max(dfs(0), dfs(1))






        