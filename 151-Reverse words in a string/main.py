from typing import List, Tuple

class Solution:
    def reverseWords(self, s: str) -> str:
        output: List[str] = s.split()
        l: int = 0
        r: int = len(output) - 1
        def reverseWords_helper(l, r):
            if l > r:
                return
            else:
                tmp: str = output[l]
                output[l] = output[r]
                output[r] = tmp
                return reverseWords_helper(l + 1, r - 1)
        reverseWords_helper(l, r)
        return " ".join(output)
    
    
solution = Solution()
s = "the sky is blue"
print(solution.reverseWords(s))