class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = set()
        def run_nums(comb, soma):
            if soma > target:
                return 
            elif soma == target:
                combinations.add((tuple(sorted(comb))))
            elif soma < target:
                for n in nums:
                    run_nums(comb=comb+[n], soma=soma+n)

        run_nums([], 0)
        print(combinations)

        return [list(comb) for comb in combinations]
        