class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(bin(n).replace('0b', ''))
        x = '0'*(32-len(x)) + x
        x = x[::-1]
        return int(x,2)
        