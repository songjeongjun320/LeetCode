class Solution():
    def searchInsert(self, nums, target):
        for _ in range(len(nums)):
            if target <= nums[_]:
                return _
        return len(nums)