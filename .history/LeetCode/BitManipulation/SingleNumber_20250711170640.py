class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result


#The property of XOR is that it cancels out the same numbers,
#so the result will be the number that appears only once in the array.        