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
        
        