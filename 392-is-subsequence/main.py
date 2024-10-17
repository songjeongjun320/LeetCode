from typing import List, Tuple

class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        l: int = 0
        for i in range(len(s)):
            tmp: int = t.find(s[i],l,len(t))
            if tmp == -1:
                return False
            l = tmp + 1
            
        return True

sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))