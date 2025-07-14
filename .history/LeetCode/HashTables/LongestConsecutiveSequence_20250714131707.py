class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        print(s)
        longest=0
        for n in s:
            if n-1 not in s:
                length=1
                while n+length in s:
                    length+=1
                longest=max(longest,length)
        return longest
        
# This code finds the length of the longest consecutive sequence in an unsorted array.
# It uses a set to store unique numbers and checks for consecutive sequences starting from each number.
