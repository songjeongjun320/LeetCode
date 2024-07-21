from typing import List, Tuple

class Solution():
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = []
        zero_count: int = 0
        zero_position: int = 0
        total_product: int = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
    
                if zero_count == 2:
                    for i in range(len(nums)):
                        output.append(0)
                    return output
                continue
            else:
                total_product *= nums[i]
        
        if zero_count == 1:
            zero_position = nums.index(0)
            for i in range(len(nums)):
                if i != zero_position:
                    output.append(0)
                else:
                    tmp = 1
                    for j in range(len(nums)):
                        if j == zero_position:
                            continue
                        tmp *= nums[j]
                    output.append(tmp)
            return output
        
        else:
            for num in nums:
                output.append(total_product // num)
                
        return output


solution = Solution()
nums: List[int] = [1,2,3,4]
print(solution.productExceptSelf(nums))