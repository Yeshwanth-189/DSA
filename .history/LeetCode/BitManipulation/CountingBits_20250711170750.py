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