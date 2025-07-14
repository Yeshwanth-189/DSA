class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if magazine==ransomNote:
            return True

        ch={}
        for c in magazine:
            ch[c]=ch.get(c,0)+1
        for c in ransomNote:
            if c not in ch or ch[c]==0:
                return False
            else:
                ch[c]-=1
        return True
        

# It uses a dictionary to count the occurrences of each character in the magazine.
# If a character in the ransom note is not available in sufficient quantity in the magazine, it returns False.