from typing import List, Tuple

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            word1_set: set = set(word1)
            word2_set: set = set(word2)
            print(word1_set)
            print(word2_set)
            if word1_set != word2_set:
                return False
            tmp1: List[int] = []
            tmp2: List[int] = []
            word1_list: List[int] = list(word1_set)
            for i in range(len(word1_set)):
                tmp1.append(word1.count(word1_list[i]))
                tmp2.append(word2.count(word1_list[i]))
            i: int = 0
            tmp1.sort()
            tmp2.sort()
            for i in range(len(tmp1)):
                if tmp1[i] != tmp2[i]:
                    return False
                
        return  True
    
word1: str = "aabbcccddd"
word2: str = "abccccdddd"
sol = Solution()
print(sol.closeStrings(word1, word2))