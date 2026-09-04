class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = collections.defaultdict(int)

        for i in nums:
            dict_nums[i]+=1
        
        orderd_dict = dict(sorted(dict_nums.items(), key=lambda r:r[1], reverse=True))

        return list(orderd_dict.keys())[:k]
        