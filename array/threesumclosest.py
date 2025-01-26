from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")
        high = len(nums) - 1 
        ans = float("inf")
        for k in range(high-1):
            i = k+1
            j = high
            num = nums[k]
            remain = target - num
            while i < j:
                current_sum = nums[i] + nums[j]
                current_closest = min(closest_sum, abs(remain - current_sum))
                if current_closest < closest_sum:
                    closest_sum = current_closest
                    ans = current_sum + num
                if current_sum == remain:
                    return ans
                elif current_sum > remain:
                    j -= 1
                elif current_sum < remain:
                    i += 1
        return ans


if __name__ == "__main__":
    nums = [-1,2,1,-4]
    print(Solution().threeSumClosest(nums, -4))