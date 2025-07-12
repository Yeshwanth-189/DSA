class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift=0
        while left!=right:
            left>>=1
            right>>=1
            shift+=1
        return left<<shift

#It shifts both numbers to the right until they are equal, counting the number of shifts, and then shifts the result back to the left by that count to get the final result.        