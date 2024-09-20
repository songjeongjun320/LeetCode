from typing import List, Tuple, Optional

class Solution:
    def pairs(self, input_list:List[int], n: int):
        output:List[List[int]] = []
        for i in range(n-1):
            tmp:List[int] = []
            for j in range(i + 1, n):
                if input_list[i] > 2 * input_list[j]:
                    tmp.append(i+1)
                    tmp.append(j+1)
                    output.append(tmp)
                    tmp = []
        return output


sol: Solution = Solution()
tmp_list: List[int] = [4,5,8,10,2,1,7,3]
output_list = sol.pairs(tmp_list, len(tmp_list))
print(output_list)
print(len(output_list))