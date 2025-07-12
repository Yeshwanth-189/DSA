class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return nums
        result=0
        for i in nums:
            result^=i
        diff=result & -result
        x,y=0,0
        for num in nums:
            if num & diff:
                x=x^num
            else:    
                y=y^num
        return [x,y]
        
# This solution uses the XOR operation to find the two unique numbers in the array. It first computes the XOR of all numbers, which gives a result that is the XOR of the two unique numbers. 
# Then, it finds a bit that is set in this result (using `result & -result`), which helps to partition the numbers into two groups based on whether they have this bit set or not. Finally, it computes the XOR for each group to find the two unique numbers.        