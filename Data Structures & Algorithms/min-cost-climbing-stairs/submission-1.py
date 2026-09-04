class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        zero_index = 0
        first_index = 0
        mem = {}
        def step(index):
            if index > len(cost) - 1: return 0
            if mem.get(index): return mem[index]

            one_step = cost[index] + step(index+1)
            two_step = cost[index] + step(index+2)
            mem[index] = min(one_step, two_step)
            return mem[index]
        
        zero_index = step(0)
        first_index = step(1)

        return min(zero_index, first_index)
        