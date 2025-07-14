class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # def isSubsequence(s: str, t: str) -> bool:
        #     if s=="":
        #         return True
        #     if s==t:
        #         return True
        #     n=len(s)
        #     m=len(t)
        #     i,j=0,0
        #     while i<n and j<m:
        #         if s[i]==t[j]:
        #             i+=1
        #         j+=1
        #     return i==n   

        # count=0
        # n=len(s)
        # for word in words:
        #     if isSubsequence(word,s):
        #         count+=1
        # return count

        output=0
        s_map=defaultdict(list)

        for i,c in enumerate(s):
            s_map[c].append(i)

        for w in words:
            prev=-1
            found=True
            for c in w:
                x=bisect.bisect(s_map[c],prev)
                if x==len(s_map[c]):
                    found=False
                    break
                else:
                    prev=s_map[c][x]
            if found:
                output+=1
        return output
        
# This code counts the number of words in the list that are subsequences of the string s.
# It uses a dictionary to map characters to their indices in s, allowing for efficient checking of subsequences.

#Optimization:
# Use bucketing to group words by their first character.
# Check the waiting list for each character in s.