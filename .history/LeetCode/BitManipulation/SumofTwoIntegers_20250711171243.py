class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b!=0:
            carry=(a & b) & MASK
            a=(a^b) & MASK
            b=(carry<<1) & MASK
        return a if a<=MAX_INT else ~(a ^ MASK)
        
# This solution uses bitwise operations to compute the sum of two integers without using the '+' operator. 
# It repeatedly calculates the carry and updates the values of a and b until there are no more carries left. The final result is adjusted to handle negative numbers correctly by checking if the result exceeds the maximum integer value.
# The use of MASK ensures that the operations are performed within the bounds of a 32-bit signed integer, and the final adjustment handles the case where the result is negative by flipping the bits and adding one (two's complement representation).        