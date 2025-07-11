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
        