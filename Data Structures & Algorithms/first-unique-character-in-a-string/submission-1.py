class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = collections.defaultdict(int)
        for i in s:
            s_dict[i] += 1
        
        for k, v in enumerate(s):
            if s_dict[v] == 1: return k
        return -1