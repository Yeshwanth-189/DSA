class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=a+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
        return ans
        
# It uses a two-pointer technique after sorting the array to efficiently find the triplets.
# The algorithm iterates through the sorted list, fixing one element and using two pointers to find pairs that sum to zero. 
# The solution avoids duplicates by skipping over repeated elements.