class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        def step(index):
            if index > len(cost) - 1: return 0
            if mem.get(index): return mem[index]

            one_step = cost[index] + step(index+1)
            two_step = cost[index] + step(index+2)
            mem[index] = min(one_step, two_step)
            return mem[index]

        return min(step(0), step(1))
        