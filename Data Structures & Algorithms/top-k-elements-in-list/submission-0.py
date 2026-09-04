class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = collections.defaultdict(int)
        for i in nums:
            nums_dict[i] += 1
        
        nums_dict = sorted(nums_dict.items(), key=lambda r:r[1], reverse=True)

        nums_list = [nums_dict[i][0] for i in range(k)]

        return nums_list
        