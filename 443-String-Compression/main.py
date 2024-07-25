from typing import List, Tuple

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev: int = 0
        curr: int = 0
        cnt: int = 1
        write: int = 0

        while curr < len(chars):
            if prev == curr:
                curr += 1
                            

        return write


chars = ["a","a","b","b","c","c","c"]
sol = Solution()
print(sol.compress(chars))