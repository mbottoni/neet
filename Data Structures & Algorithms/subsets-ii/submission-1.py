class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bin_numbers(n):
            subsets_idx = []
            for i in range(n):
                bin_rep = str(bin(i)).replace('0b', '')
                diff = len(nums) - len(bin_rep)
                bin_rep = diff*'0' + bin_rep
                subsets_idx.append(bin_rep)
            return subsets_idx

        subsets_idx = bin_numbers(2**len(nums))
        combinations = set()
        for comb in subsets_idx:
            c = []
            for j in range(len(nums)):
                if comb[j] == '1':
                    c.append(nums[j])
            combinations.add(tuple(sorted(c)))

        return [list(comb) for comb in combinations]

        