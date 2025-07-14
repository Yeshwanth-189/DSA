class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c={}
        for i in range(len(text)):
           c[text[i]]=c.get(text[i],0)+1

        required={'n': 1, 'l': 2, 'a': 1,'b': 1, 'o': 2}

        min_ballon=float('inf')
        for ch in required:
            if ch not in c:
                return 0
            min_ballon=min(min_ballon,c[ch]//required[ch])
        return min_ballon
# This code counts the occurrences of characters in the input string and calculates how many times the word "balloon" can be formed based on the required character counts.
# It returns the minimum number of complete "balloon" words that can be formed.        