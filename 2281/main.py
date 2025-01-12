from typing import List, Tuple

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        result = 0
        l = 0
        r = 0

        # sum of all elements from the start to the current index
        prefix: List[int] = []
        prefix.append(strength[0])
        for _ in range(1,len(strength)):
            prefix.append(prefix[_ - 1] + strength[_])

        # _ denote the length between l and r
        for _ in range(0, len(strength)):
            print("======================")
            print("length: ", _)
            r = l + _
            sum_tmp_array = 0

            # To reduce the bigO, make remember the sum and update it subtract strength[l] and add strength[r+1]
            # It will make O(n) to O(log(n))
            while r < len(strength):
                # First sum from l to r should be calculated at once and store it sum variable
                if l == 0:
                    sum_tmp_array = prefix[r]
                else:
                    sum_tmp_array = prefix[r] - prefix[l-1]
                print("sum: ", sum_tmp_array)
                print("sum: ", sum_tmp_array)
                tmp_strength = strength[l:r+1]
                print("tmp_strength: ", tmp_strength)
                result += min(tmp_strength) * sum_tmp_array
                print("result: ", result)
                r += 1
                l += 1
            l = 0
        return result % MOD

sol: Solution = Solution()
strength = [1,3,1,2]
print("total_length: ", len(strength))
print(sol.totalStrength(strength))

