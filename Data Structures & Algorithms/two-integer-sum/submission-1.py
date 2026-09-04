class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_of_numbers = []

        for index, i in enumerate(nums):
            if target - i in list_of_numbers:
                return [nums.index(target - i), nums.index(i, index)]
            list_of_numbers.append(i)