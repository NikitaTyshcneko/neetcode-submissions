class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        minimum = (0, 0)
        min_length = float("inf")
        
        counter1 = collections.Counter(t)
        counter2 = {}
        window = {}

        need = len(counter1)
        have = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in counter1 and window[s[r]] == counter1[s[r]]:
                have +=1

            while have == need:
                if r - l + 1 < min_length:
                        min_length = r - l + 1
                        minimum = (l, r + 1)

                window[s[l]] -= 1
                if s[l] in counter1 and window[s[l]] < counter1[s[l]]:
                    have -= 1

                l += 1
                
        
        return s[minimum[0]:minimum[1]]


        