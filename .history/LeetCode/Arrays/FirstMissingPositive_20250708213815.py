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

        
        
## This solution uses the Inplace-hashing/cyclic sort technique to place each number in its correct position.
# It iterates through the array and swaps elements until each number is either out of range or        
        

        