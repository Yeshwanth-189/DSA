class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for word in strs[1:]:
                if i>=len(word) or word[i]!=ch:
                    return prefix
            prefix+=ch
        return prefix
# This solution iterates through the characters of the first string and checks if they match in all other strings.
# If a mismatch is found or the end of any string is reached, it returns the accumulated        