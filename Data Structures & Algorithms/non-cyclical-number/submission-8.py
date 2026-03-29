class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0 
        vis = set()
        while True:
            i = 0
            for digit in str(n):
                i = i + int(digit)**2
            n = i

            if n == 1:
                return True

            if n in vis:  # removed redundant `and i!=1`
                return False

            vis.add(n)  # add this line

        return False