class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0 
        digits = digits[::-1]
        for i in range(len(digits)):
            if i==0:
                soma = (digits[i]+1+carry) % 10
                carry = (digits[i]+1+carry) // 10 
                digits[i] = soma
            else:
                soma = (digits[i]+carry) % 10
                carry = (digits[i]+carry) // 10
                digits[i] = soma
                
        if carry > 0:
            digits = digits+[1]
            
        return digits[::-1]