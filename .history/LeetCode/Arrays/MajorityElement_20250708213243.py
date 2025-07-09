class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element=None
        count=0
        for num in nums:
            if count==0:
                majority_element=num
            if num==majority_element:
                count+=1
            else:
                count-=1
        return majority_element
        

# This is the Boyer-Moore Voting Algorithm, which finds the majority element in linear time and constant space.
# The algorithm works by maintaining a count of the current candidate for majority element.        