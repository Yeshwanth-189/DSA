class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()               
        words.reverse()               
        return " ".join(words)
               
# This solution splits the string into words, reverses the list of words, and then joins them back into a single string.        