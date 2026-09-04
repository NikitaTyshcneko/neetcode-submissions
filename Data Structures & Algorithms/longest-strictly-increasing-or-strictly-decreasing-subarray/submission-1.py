class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 0
        previous = -1
        is_incresing = True
        increasing_max = 0
        decreasing_max = 0
        for i in nums:
            if i > previous:
                if not is_incresing: longest = 1
                is_incresing = True
                longest+=1
            elif i < previous:
                if is_incresing: longest = -1
                is_incresing = False
                longest-=1
            else:
                longest = 0
            
            if increasing_max < longest:
                increasing_max = longest
            elif decreasing_max > longest:
                decreasing_max = longest
            previous = i
        
        return abs(decreasing_max) if abs(decreasing_max) > increasing_max else increasing_max
        