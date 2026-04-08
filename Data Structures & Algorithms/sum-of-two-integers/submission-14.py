class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 1. Handle 32-bit overflow using a mask
        mask = 0xFFFFFFFF
        
        # 2. Use bitwise logic to simulate addition instead of strings
        # This is the standard "Low-Level" approach for this problem
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        # 3. If 'a' is negative, handle the 32-bit sign extension
        return (a & mask) if b > 0 else a