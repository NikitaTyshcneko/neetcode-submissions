class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
            
        for i in nums:
            new_list = []
            for j in result:
                new_list.append(j+[i])
            result+=new_list
        return result