from typing import List, Tuple

class Solution:
    def compress(self, chars: List[str]) -> int:
        i: int = 0
        j: int = 0
        cnt: int = 0
        output: str = ""

        if len(chars) == 1 :
            return 1

        while i < len(chars):
            while j < len(chars):
                if chars[i] == chars[j]:
                    if j == len(chars) - 1:
                        output += chars[i]
                        i = j
                        i += 1
                    cnt += 1
                else:
                    output += chars[i]
                    if cnt != 1:
                        output += str(cnt)
                    cnt = 0
                    i = j
                    break
                j += 1
            if j == len(chars):
                if cnt != 1:
                    output += str(cnt)


        for i in range(len(output)):
            chars[i] = output[i]
        print(output)
        return len(output)


chars = ["a","a","b","b","c","c","c"]
sol = Solution()
print(sol.compress(chars))