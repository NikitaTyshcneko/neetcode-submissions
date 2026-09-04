class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        slow = 0
        for fast in range(len(prices)):
            if prices[fast]<prices[slow]:
                slow = fast
            max_value = max(max_value, prices[fast]-prices[slow])
        return max_value
        