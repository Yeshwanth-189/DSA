class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for i in range(32):
            ans= (ans<<1) | (n & 1)
            n>>=1
        return ans

        
# This solution iterates through each bit of the integer n, shifting the bits of ans to the left and adding the least significant bit of n to ans. The process continues until all 32 bits have been processed, effectively reversing the bits of n.        