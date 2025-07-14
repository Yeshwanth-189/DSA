class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexS = [0] * 256
        indexT = [0] * 256
        
        length = len(s) 
        
        for i in range(length): 
            if indexS[ord(s[i])] != indexT[ord(t[i])]: 
                return False 
            
            indexS[ord(s[i])] = i + 1 
            indexT[ord(t[i])] = i + 1
        
        return True 



        

# It uses two arrays to track the last seen index of each character in both strings.
# If the mapping is consistent throughout the strings, it returns True; otherwise, it returns False