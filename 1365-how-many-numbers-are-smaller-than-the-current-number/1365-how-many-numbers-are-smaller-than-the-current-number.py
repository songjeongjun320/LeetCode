class Solution():
    def smallerNumbersThanCurrent(self, nums):
        output = []
        tmp = 0
        for _ in range(len(nums)):
            for j in range(len(nums)):
                if _ != j and nums[_] > nums[j]:
                    tmp += 1
            output.append(tmp)
            tmp = 0
        return output
                    
        