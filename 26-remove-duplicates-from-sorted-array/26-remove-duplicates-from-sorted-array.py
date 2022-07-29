class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return False
        
        count = 1
        for _ in range(len(nums)-1):
            if nums[_] != nums[_+1]:
                nums[count] = nums[_+1]
                count += 1
        return count
