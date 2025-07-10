class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        if s==t:
            return True
        n=len(s)
        m=len(t)
        i,j=0,0
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==n        
        

# This solution uses two pointers to check if all characters of s appear in t in the same order.
# It iterates through both strings, moving the pointer in s only when a matching character is found       