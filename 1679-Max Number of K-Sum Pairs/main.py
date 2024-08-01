from typing import List, Tuple

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        list: List[int] = nums.copy()
        list.sort()

        l: int = 0
        result: int = 0

        while l <= len(list) - 2:
            if list[l] >= k:
                list.pop(l)
                continue
            l_plus: bool = True
            for r in range(len(list)-1, l, -1):
                if r == l:
                    l_plus = False
                if list[r] > k:
                    list.pop(r)
                    continue
                if list[l] + list[r] < k:
                    break
                if list[l] + list[r] == k:
                    list.pop(r)
                    list.pop(l)
                    result += 1
                    l_plus = False
                    break
            if l_plus:
                l += 1

        return result


sol = Solution()
nums: int = [3,5,1,5]
k: int = 2
print(sol.maxOperations(nums,k))