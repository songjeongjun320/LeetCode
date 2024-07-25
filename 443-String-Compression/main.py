from typing import List, Tuple

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev: str = ""
        curr: int = 0
        cnt: int = 1
        write: int = 0

        while curr < len(chars):
            if prev != chars[curr]:
                chars[write] = prev
                prev = chars[curr]
                write += 1
                if cnt != 1:
                    chars[write] = str(cnt)
                    write += 1
                    cnt = 1
            else:
                cnt += 1
            curr += 1
                

        return write


chars = ["a","a","b","b","c","c","c"]
sol = Solution()
print(sol.compress(chars))