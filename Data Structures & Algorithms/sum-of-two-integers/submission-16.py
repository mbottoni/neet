class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b & mask:
            tmp = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = tmp
        
        # If sign bit is set, convert back to negative
        return a if a < 0x80000000 else ~(a ^ mask)