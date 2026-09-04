class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = collections.defaultdict(int)
        for i in s:
            s_dict[i] += 1
        
        for k, v in s_dict.items():
            if v == 1: return s.index(k)
        return -1