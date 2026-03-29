class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possible_count = 2**len(nums)
        n = len(nums)
        permutations = []
        for i in range(possible_count):
            perm = str(bin(i)).replace('0b', '')
            n_perm = len(perm)
            diff = n - n_perm
            perm = "0" * diff + perm

            permute = []
            for j in range(len(perm)):
                if perm[j] == "1":
                    permute.append(nums[j])
            permutations.append(permute)
        return permutations
                

        