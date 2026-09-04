class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        empty_array = []
        for i in nums1:
            index = nums2.index(i)
            while index < len(nums2):
                if nums2[index] > i:
                    empty_array.append(nums2[index])
                    break
                index+=1
            else:
                empty_array.append(-1)
        return empty_array
            
