class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def char_count_signature(st):
            count = [0] * 26  
            for c in st:
                count[ord(c) - ord('a')] += 1
            return tuple(count)  
        
        anagram_map = defaultdict(list)
        
        for st in strs:
            sig = char_count_signature(st)
            anagram_map[sig].append(st)
        
        return list(anagram_map.values())
        

# This code groups anagrams by creating a character count signature for each string.
# It uses a dictionary to map these signatures to lists of anagrams.