class Solution:
    def countBits(self, n: int) -> List[int]:

        #brute-force
        """ans=[0]*(n+1)
        for i in range(n+1):
            num=i
            count=0
            while num:
                if num & 1:
                    count+=1
                num>>=1
            ans[i]=count
        return ans"""

        #optimal
        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i>>1]+(i&1)
        return ans

# This solution uses dynamic programming to build the count of 1 bits for each number from 0 to n based on previously computed values. The expression `i >> 1` shifts the bits of i to the right, effectively dividing it by 2, and `(i & 1)` checks if the least significant bit is 1. This approach is more efficient than the brute-force method.