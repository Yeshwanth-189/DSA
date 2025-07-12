class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            if n & 1 == 1:
                count+=1
            n>>=1
        return count

# This solution uses bitwise operations to count the number of 1 bits in the binary representation of the integer n.        