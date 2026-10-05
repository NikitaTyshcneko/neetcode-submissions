class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            max1 = stones.pop(stones.index(max(stones)))
            max2 = stones.pop(stones.index(max(stones)))
            if max1>max2: stones.append(max1-max2)
        
        if len(stones) == 0: return 0
        return stones[0]
        