class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = set()
        def run_nums(comb, soma, possibles):
            if soma > target:
                return 
            elif soma == target:
                combinations.add((tuple(sorted(comb))))
            elif soma < target:
                for i in range(len(possibles)):
                    run_nums(comb=comb+[possibles[i]], soma=soma+possibles[i], possibles=possibles[:i]+possibles[i+1:])

        run_nums([], 0, nums)
        print(combinations)
        return [list(comb) for comb in combinations]
        