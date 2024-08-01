from typing import List, Tuple

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum: int = 0
        max_sum: int = 0
        for i in range(k):
            sum += nums[i]
        max_sum = sum

        for i in range(1, len(nums) - (k - 1)):
            sum -= nums[i - 1]
            sum += nums[i + k - 1]

            if sum > max_sum:
                max_sum = sum
        return max_sum/k

sol = Solution()
nums: list[int] = [1,12,-5,-6,50,3]
k: int = 4
print(sol.findMaxAverage(nums,k))
