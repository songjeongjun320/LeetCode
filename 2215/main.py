from typing import List, Tuple

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1: List[int] = []
        n2: List[int] = []
        for i in nums1:
            if not i in n1:
                n1.append(i)
        for i in nums2:
            if not i in n2:
                n2.append(i)
        i: int = 0
        while i < len(n1):
            if n1[i] in n2:
                n2.remove(n1[i])
                n1.pop(i)
                i -= 1
            i += 1
        return [n1, n2]


nums1: List[int] = [1,2,3]
nums2: List[int] = [2,4,6]
sol: Solution = Solution()
print(sol.findDifference(nums1, nums2))