class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        length = len(nums)
        if length == 1:
            return nums[0]
        
        _ = 0
        while _ <= length-1:
            if nums[_] == nums[_+1]:
                _+=2
                if _ == length-1:
                    return nums[_]
            else:
                if nums[_+1] == nums[_+2]:
                    return nums[_]