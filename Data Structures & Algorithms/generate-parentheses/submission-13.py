class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = set()
        def gen(comb, op, cl):
            if op > 0:
                gen(comb=comb + "(", op = op - 1 , cl = cl)
            if cl < n - op:  # fixed condition
                gen(comb=comb + ")", op = op, cl = cl + 1)

            if op==0 and cl == n:
                if comb not in combinations:
                    combinations.add(comb)


        gen("", op = n, cl = 0)
        return list(combinations)