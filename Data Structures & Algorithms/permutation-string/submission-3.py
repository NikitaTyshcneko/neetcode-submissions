class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        counter1 = collections.Counter(s1)
        counter2 = {}

        l=0
        end = len(s1)
        for r in s2:
            counter2[r] = counter2.get(r, 0) + 1
            sim = True

            if sum(counter2.values()) < end: continue

            print(counter2, counter1)

            for j in s1:
                if counter2.get(j, 0) != counter1.get(j):
                    sim = False
                    break;

            if sim: return True

            counter2[s2[l]] -= 1
            l+=1
        
        return False

        