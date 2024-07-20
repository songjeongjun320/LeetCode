from typing import List, Tuple

class Solution:
    def reverseVowels(self, s: str) -> str:
        l: int = 0
        r: int = len(s) - 1
        result: List[str] = list(s)
        vowels: List[str] = ['a','e','i','o','u','A','E','I','O','U']

        def reverseVowels_helper(l, r):
            if l > r:
                return
            if not result[l] in vowels:
                l += 1
                return reverseVowels_helper(l, r)
            if not result[r] in vowels:
                r -= 1
                return reverseVowels_helper(l, r)
            if result[l] in vowels and result[r] in vowels:
                tmp = result[l]
                result[l] = result[r]
                result[r] = tmp
                l += 1
                r -= 1
                return reverseVowels_helper(l, r)

        reverseVowels_helper(l, r)
        
        return ''.join(result)


solution = Solution()
s: str = "hello"
print(solution.reverseVowels(s))