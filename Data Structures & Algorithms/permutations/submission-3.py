class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        def perm(arr, comb):
            if len(arr) > 0:
                for i in range(len(arr)):
                    perm(arr[:i]+arr[i+1:], comb+[arr[i]])
            else:
                combinations.append(comb)

        perm(nums, [])
        return combinations

