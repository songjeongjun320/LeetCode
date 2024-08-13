from typing import List, Tuple

class Solution:
    def removeStars(self, s: str) -> str:
        output:List[str] = []

        for item in s:
            if item != '*':
                output.append(item)
            else:
                output.pop()

        return ''.join(output)
    
sol: Solution = Solution()
s: str = ""
print(sol.removeStars(s))