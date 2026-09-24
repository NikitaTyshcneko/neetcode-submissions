class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0
        l = 0
        longest = 1
        symbols_dict = {}
        for r in range(len(s)):
            if l <= symbols_dict.get(s[r], -1):
                l = symbols_dict[s[r]] + 1
            else:
                longest = max(longest, r-l+1)
            
            symbols_dict[s[r]] = r
        
        return longest
        