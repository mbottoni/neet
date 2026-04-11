class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # minimum possible open parens
        high = 0  # maximum possible open parens

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1   # * acts as )
                high += 1  # * acts as (

            if high < 0:  # too many ) even in best case
                return False
            low = max(low, 0)  # can't have negative open parens

        return low == 0