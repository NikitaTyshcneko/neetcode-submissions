class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        longest = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxf = max(maxf, counter[s[r]])

            while r-l+1-maxf>k:
                counter[s[l]] = counter[s[l]]-1
                l+=1
            
            longest = max(longest, r-l+1)
        
        return longest

                    

        