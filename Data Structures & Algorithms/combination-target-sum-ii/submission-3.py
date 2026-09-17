class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        list_resultes = set()
        candidates.sort()

        def dfs(i, sums, array_set):
            if sums == target:
                list_resultes.add(tuple(array_set))
                return
            if i == len(candidates) or sums > target:
                return

            array_set.append(candidates[i])
            dfs(i+1, sums+candidates[i], array_set)
            array_set.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i+1, sums, array_set)
        
        array_set = []
        dfs(0, 0, array_set)
        
        return [list(combination) for combination in list_resultes]
        