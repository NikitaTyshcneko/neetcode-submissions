class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        counter1 = collections.Counter(s1)

        window = len(s1)
        s1_sorted = sorted(s1)

        l=0
        r = window
        while r<len(s2)+1:
            subcounter2 = collections.Counter(s2[l:r])
            if subcounter2 == counter1: return True
            l+=1
            r+=1
        
        return False

        