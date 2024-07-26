from typing import List, Tuple

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        prev: int = 0
        curr: int = 0
        cnt: int = 1
        write: int = 0
        output: str = ""

        while curr < len(chars) - 1:
            if prev == curr:
                output += chars[prev]
                curr += 1
            if chars[prev] == chars[curr]:
                cnt += 1
            else:
                if cnt != 1:
                    output += str(cnt)
                    cnt = 1
                prev = curr 
                continue
            prev += 1
            curr += 1
        if chars[prev] == chars[curr]:
            cnt += 1
            output += str(cnt)
        else:
            output += str(cnt)

        for i in range(len(output)):
            chars[i] = output[i]
        return chars


chars = ["a","a","a","b","b","a","a"]
sol = Solution()
print(sol.compress(chars))