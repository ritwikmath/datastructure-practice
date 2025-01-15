from typing import List

nums = [-1, 0, 3, 44, 77, 102]

target = 77

class Solution:
    def search(self, nums: List[int], target: int):
        list_length = len(nums)
        left_pointer = 0
        right_pointer = list_length - 1
        pointer = -1
        while pointer == -1:
            median = (left_pointer + right_pointer) // 2
            current_value = nums[median]
            if target == current_value:
                pointer = median
            elif right_pointer == left_pointer and target == nums[left_pointer]:
                pointer = left_pointer
            elif right_pointer <= left_pointer:
                break
            elif target > current_value:
                left_pointer = median + 1
            elif target < current_value:
                right_pointer = median -1
            
        return pointer
    
print(Solution().search(nums, target))
