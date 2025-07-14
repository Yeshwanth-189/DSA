class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum==target:
                return [i+1,j+1]
            elif curr_sum<target:
                i+=1
            else:
                j-=1
        
        return []

# This code uses a two-pointer technique to find two numbers in a sorted list that add up to a target value.

# The pointers start at the beginning and end of the list and move towards each other based on the current sum compared to the target.