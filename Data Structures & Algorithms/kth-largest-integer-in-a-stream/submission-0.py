class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.index = k-1
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums, reverse=True)[self.index]


        
