from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for char in strs :
            count=[0]*26
            for c in char :
                count[ord(c)-ord("a")]+=1
            anagram_map[tuple(count)].append(char)
        return list(anagram_map.values())