from typing import List, Tuple

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel: list[str] = ['a', 'e', 'i', 'o', 'u']
        max_vowel: int = 0
        curr_vowel: int = 0

        for i in range(k):
            if s[i] in vowel:
                max_vowel += 1
        curr_vowel = max_vowel

        for i in range(1, len(s) - k + 1):
            if s[i-1] in vowel:
                curr_vowel -= 1
            if s[i + k - 1] in vowel:
                curr_vowel += 1
            if curr_vowel >= max_vowel:
                max_vowel = curr_vowel
                if max_vowel == k:
                    break

        return max_vowel

sol = Solution()
s: str = "weallloveyou"
k: int = 7
print(sol. maxVowels(s,k))