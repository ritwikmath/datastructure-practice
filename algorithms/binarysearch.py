from typing import List

nums = [-1, 0, 3, 44, 77, 102]

target = 0

class Solution:
    def search(self, nums: List[int], target: int):
        list_length = len(nums)
        left_pointer = 0
        right_pointer = list_length - 1
        while right_pointer >= left_pointer:
            median = (left_pointer + right_pointer) // 2
            current_value = nums[median]
            if target == current_value:
                return median
            elif target > current_value:
                left_pointer = median + 1
            elif target < current_value:
                right_pointer = median -1

        return -1
    
print(Solution().search(nums, target))
