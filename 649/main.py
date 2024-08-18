from typing import List, Tuple

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cnt: int = len(senate)
        r_list: List[int] = []
        d_list: List[int] = []
        for i in range(len(senate)):
            if senate[i] == 'R':
                r_list.append(i)
            else:
                d_list.append(i)

        while True:
            if len(r_list) == 0 or len(d_list) == 0:
                break
            if r_list[0] < d_list[0]:
                r_list.pop(0)
                d_list.pop(0)
                r_list.append(cnt)
            else:
                r_list.pop(0)
                d_list.pop(0)
                d_list.append(cnt)           
            cnt += 1
                

        if len(r_list) == 0:
            return "Dire"
        else:
            return "Radiant"
    
sol:Solution = Solution()
senate: str = "DDRRR"
print(sol.predictPartyVictory(senate))
