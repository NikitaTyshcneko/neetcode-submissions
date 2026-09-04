class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = collections.defaultdict(list)

        for word in strs:
            anagrams_dict[''.join(sorted(word))].append(word)
        
        return list(anagrams_dict.values())
        