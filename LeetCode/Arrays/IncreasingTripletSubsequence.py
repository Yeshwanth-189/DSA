class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        first=float('inf')
        second=float('inf')
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            elif num>second:
                return True
        return False
        
# This solution iterates through the array and keeps track of the first and second smallest elements.
# If a number greater than the second smallest is found, it indicates the presence of an increasing triplet subsequence.        