class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """ Brute Force
        count=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count"""
        
        index_map = defaultdict(list)
        count = 0

        for i, num in enumerate(nums):
            if index_map[num]:  
                count+=len(index_map[num])
            index_map[num].append(i)

        return count

# It uses a dictionary to store indices of each number and counts pairs based on previously seen indices
