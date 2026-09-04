class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        previous = -1
        sum_result = 0
        current_sum = 0

        for i in nums:
            if i > previous:
                current_sum += i
                sum_result = max(current_sum, sum_result)
            else:
                current_sum = i
            previous = i
        return sum_result
        