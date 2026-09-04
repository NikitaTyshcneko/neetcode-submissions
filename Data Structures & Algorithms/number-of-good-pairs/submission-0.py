class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_nums = {}
        good_pair = 0
        for i in nums:
            if dict_nums.get(i) is not None:
                dict_nums[i]['count'] += 1
                dict_nums[i]['value'] += dict_nums[i]['count'] - 1
            else: 
                dict_nums[i] = {'value': 0, 'count': 1}
        
        total_sum = 0
        
        for i in dict_nums.values():
            total_sum+=i['value']
        
        return total_sum

        