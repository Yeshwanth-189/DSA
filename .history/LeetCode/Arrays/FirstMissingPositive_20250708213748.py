class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                correct_index=nums[i]-1
                nums[correct_index],nums[i]=nums[i],nums[correct_index]
        for i in range(n):
            if i+1!=nums[i]: 
                return i+1
        return n+1       

        
        
        
        

        