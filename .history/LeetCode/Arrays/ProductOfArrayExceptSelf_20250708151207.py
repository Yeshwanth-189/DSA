class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """With Extra Space
        n=len(nums)
        prefix=[1]*n
        prefix[0]=1
        for i in range(n-1):
            prefix[i+1]=prefix[i]*nums[i]
        
        suffix=[1]*n
        suffix[n-1]=1
        for i in range(n-1,0,-1):
            suffix[i-1]=suffix[i]*nums[i]
        for i in range(n):
            nums[i]=prefix[i]*suffix[i]
        return nums"""
            

        n=len(nums)
        answer=[1]*n
        prefix=1
        suffix=1
        for i in range(1,n):
            prefix*=nums[i-1]
            answer[i]=prefix
        for i in range(n-2,-1,-1):
            suffix*=nums[i+1]
            answer[i]*=suffix
        return answer