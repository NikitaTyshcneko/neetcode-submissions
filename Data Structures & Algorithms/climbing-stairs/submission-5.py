class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=3: return n

        current=3
        previous1 = 2
        previous2 = 0

        for i in range(4, n+1):
            previous2 = previous1
            previous1 = current
            current = previous2 + previous1
        return current


        