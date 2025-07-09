class Solution:
    def reverse(self,nums:List[int],start:int,end:int)->None:
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)

        

# This solution uses the reverse method to rotate the array in place.
# It first reverses the entire array, then reverses the first k elements and the remaining elements separately.
# This effectively rotates the array to the right by k positions without using extra space.        
        