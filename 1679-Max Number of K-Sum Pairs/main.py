from typing import List, Tuple

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        list: List[int] = nums.copy()
        l: int = 0
        result: int = 0
        
        i:int = 0
        while i < len(list):
            if list[i] >= k:
                list.pop(i)
            else:
                i += 1

        while l <= len(list) - 2:
            tmp: int = 0
            try:
                tmp = list.index(k - list[l], l + 1)
                list.pop(tmp)
                list.pop(l)
                result += 1
            except:
                l += 1      

        return result


sol = Solution()
nums: int = [3,1,3,4,3]
k: int = 6
print(sol.maxOperations(nums,k))