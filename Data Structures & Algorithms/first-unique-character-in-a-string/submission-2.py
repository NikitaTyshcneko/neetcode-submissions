class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(list(s))

        for i in s:
            if counter.get(i) == 1: return s.index(i)
        return -1
        