class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            bin_rep_ones = len(str(bin(i)).replace('0b', '').replace('0', ''))
            res.append(bin_rep_ones)
        return res
        