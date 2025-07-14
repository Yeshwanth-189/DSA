class Solution:
    def numSplits(self, s: str) -> int:
        left=defaultdict(int)
        right=defaultdict(int)

        for c in s:
            right[c]+=1
        
        count=0
        for c in s:
            left[c]+=1
            right[c]-=1
            if right[c]==0:
                del right[c]
            if len(left)==len(right):
                count+=1
        return count

                
# It uses two dictionaries to keep track of character counts in the left and right parts of the string.
# The count is incremented whenever the number of unique characters in both parts is the same.  