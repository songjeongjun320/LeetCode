from typing import List, Tuple

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum: int = 0
        p_val: int = nums[0]
        r_sum: int = sum(nums) - p_val

        for i in range(len(nums)):
            if l_sum == r_sum:
                return i 
            if i == len(nums) - 1:
                break
            l_sum += p_val
            p_val = nums[i+1]
            r_sum -= p_val
        return -1


nums: List[int] = [1,2,3]
sol: Solution = Solution()
print(sol.pivotIndex(nums))