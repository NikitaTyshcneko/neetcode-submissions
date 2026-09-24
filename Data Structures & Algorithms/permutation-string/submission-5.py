class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        counter1 = [0] * 26
        counter2 = [0] * 26

        for i in s1:
            index = ord(i) - ord('a')
            counter1[index] += 1
        
        l = 0
        for r, v in enumerate(s2):
            index = ord(s2[r]) - ord('a')
            counter2[index] += 1

            if r-l+1 < len(s1): continue

            if counter1 == counter2: return True

            last_index = ord(s2[l]) - ord('a')
            counter2[last_index] -= 1
            l+=1
        
        return False

        