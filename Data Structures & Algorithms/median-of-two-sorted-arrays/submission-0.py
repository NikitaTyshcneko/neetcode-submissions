class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1)+len(nums2))//2
        temp_list = []
        i = j = 0
        while i<len(nums1) and j<len(nums2):
            if nums2[j]<nums1[i]:
                temp_list.append(nums2[j])
                j+=1
            else:
                temp_list.append(nums1[i])
                i+=1
             
        while i<len(nums1):
            temp_list.append(nums1[i])
            i+=1
        while j<len(nums2):
            temp_list.append(nums2[j])
            j+=1

        if (len(nums1)+len(nums2))%2 != 0:
            return temp_list[mid]
        return (temp_list[mid]+temp_list[mid-1])/2
