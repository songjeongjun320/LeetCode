from typing import List, Tuple

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_cnt: int = 0
        cnt: int = 0
        l: int = 0
        r: int = 0
        flip_cnt: int = 0
        
        while r < len(nums):
            if nums[r] == 0:
                flip_cnt += 1

            if flip_cnt > k:
                l += 1
                if l >= len(nums):
                    break
                if nums[l - 1] == 0:
                    flip_cnt -= 1

            if flip_cnt <= k:
                cnt = r - l + 1
                if cnt > max_cnt:
                    max_cnt = cnt
            r += 1
        return max_cnt
    
sol = Solution()
nums: list[int] = [1,1,1,0,0,0,1,1,1,1,0]
k: int = 2
print(sol.longestOnes(nums,k))