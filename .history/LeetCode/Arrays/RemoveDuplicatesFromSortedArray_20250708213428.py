class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0
        prev_element=None
        last_index=0
        for i in range(len(nums)):
            if nums[i]!=prev_element:
                unique_count+=1
                nums[last_index]=nums[i]
                last_index=unique_count
            elif nums[i]==prev_element:
                continue
            prev_element=nums[i]
        return unique_count
        
# This solution iterates through the sorted array and keeps track of the last unique element found.
# It uses a two-pointer technique to overwrite duplicates in place, ensuring that the first `unique_count` elements of `nums` are unique.        