from typing import List, Tuple

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        for i in range(1,len(nums) - 1):
            if nums[i-1] != nums[i] != nums[i+1]:
                return nums[i]
        return None

sol = Solution()
nums = [0,1,0,1,0,1,99]
print(sol.singleNumber(nums))