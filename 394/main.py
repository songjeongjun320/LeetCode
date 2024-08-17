from typing import List, Tuple

class Solution:
    def decodeString(self, s: str) -> str:
        result: List[str] = []
        for i in range(len(s)):
            result.append(s[i])
            if s[i] == ']':
                tmp: str = ""
                a: str = ""
                while True:
                    tmp = result.pop()
                    if tmp == "[":
                        break
                    if tmp != "]":
                        a = tmp + a
                cnt: int = 0
                i: int = 0
                while result[-1].isdigit():
                    cnt += int(result.pop()) * 10 ** i
                    if not result:
                        break
                    i += 1
                a *= cnt
                result.append(a)            
        return ''.join(result)
    

sol:Solution = Solution()
s = "3[a2[c]]"
print(sol.decodeString(s))

