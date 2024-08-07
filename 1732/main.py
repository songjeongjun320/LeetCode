from typing import List, Tuple

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height: int = 0
        curr: int = 0
        for i in gain:
            curr += i
            if curr > max_height:
                max_height = curr
        return max_height

sol: Solution = Solution()
nums = [1,2,3,4,5]
print(sol.largestAltitude(nums))