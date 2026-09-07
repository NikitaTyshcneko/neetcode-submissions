class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] < nums[-1]: return nums == sorted(nums)
        else: return nums == sorted(nums, reverse=True)
        