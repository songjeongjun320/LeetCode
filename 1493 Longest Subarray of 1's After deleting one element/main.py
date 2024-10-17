from typing import List, Tuple

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l: int = 0
        r: int = 0
        max_subarray: int = 0
        curr_subarray: int = 0
        zero_index: int = -1

        if not 0 in nums:
            return len(nums) - 1

        while nums[0] == 0:
            nums.pop(0)
            if len(nums) == 0:
                return 0

        while r < len(nums):
            if nums[r] == 0:
                l = zero_index + 1
                zero_index = r
            if l <= zero_index <= r:
                curr_subarray = r - l
            else:
                curr_subarray = r - l + 1
            if curr_subarray > max_subarray:
                max_subarray = curr_subarray
            r += 1

        return max_subarray


sol = Solution()
nums: List[int] = [0,0,0]
print(sol.longestSubarray(nums))