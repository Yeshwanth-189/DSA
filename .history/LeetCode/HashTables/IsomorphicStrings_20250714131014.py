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



        
        
        