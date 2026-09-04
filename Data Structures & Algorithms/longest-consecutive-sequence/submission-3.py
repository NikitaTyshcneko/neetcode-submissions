class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums.sort()
        longest_consecutive = 1
        left = 0
        previous = -99999999999
        skip = 0
        for right, value in enumerate(nums):
            if value == previous+1:
                longest_consecutive = max(longest_consecutive, right - left+1 - skip)
            elif value == previous:
                skip+=1
                continue
            else:
                left = right
                skip = 0
            previous = value
        
        return longest_consecutive

            

        