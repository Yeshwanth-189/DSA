class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        append=defaultdict(int)
        for num in nums:
            if freq[num]==0:
                continue
            if append[num]>0:
                append[num]-=1
                append[num+1]+=1
            elif freq[num+1] and freq[num+2]>0:
                freq[num+1]-=1
                freq[num+2]-=1
                append[num+3]+=1
            else:
                return False
            freq[num]-=1
        return True
        
# This code checks if it's possible to split the array into consecutive subsequences.
# It uses a frequency counter and a dictionary to track the number of subsequences that can be formed.
# If it can form valid subsequences for all elements, it returns True; otherwise, it returns False.