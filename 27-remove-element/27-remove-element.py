class Solution():
    def removeElement(self, nums, val):
        nums.sort()
        while val in nums:
            nums.remove(val)
        return len(nums)