class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, value in enumerate(nums):
            if i != value: return i
        
        return len(nums)