from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_array_length = len(nums1)
        second_array_length = len(nums2)
        i = 0
        j = 0
        merged_list = []

        while i < first_array_length and j < second_array_length:
            if nums1[i] <= nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1
        
        while i < first_array_length:
            merged_list.append(nums1[i])
            i += 1
        
        while j < second_array_length:
            merged_list.append(nums2[j])
            j += 1
        
        high_index = len(merged_list) - 1
        low_mid = high_index // 2
        if (high_index % 2) == 1:
            median = (merged_list[low_mid] + merged_list[low_mid+1])/2
        else:
            median = merged_list[low_mid]

        return median

if __name__ == "__main__":
    arr1 = [1,3,7]
    arr2 = [2,4,5,6,7]
    print(Solution().findMedianSortedArrays(arr1, arr2))