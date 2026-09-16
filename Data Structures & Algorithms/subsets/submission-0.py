class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def backtracking(number):
            nonlocal result
            new_list = []
            for i in result:
                new_list.append(i+[number])
            result+=new_list
            
        for i in nums:
            backtracking(i)
        return result