class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0
        l = 0
        longest = 1
        current_set = set(s[l])
        symbols_dict = {}
        symbols_dict[s[l]] = l
        for r in range(1, len(s)):
            if l <= symbols_dict.get(s[r], -1) < r:
                l = symbols_dict[s[r]] + 1
            else:
                longest = max(longest, r-l+1)
            
            symbols_dict[s[r]] = r
        
        return longest
        