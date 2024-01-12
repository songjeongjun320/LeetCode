class Solution(object):
    def twoSum(self, nums, target):
        switch = True
        output = []
        sum = 0
        print("Hello World")
        for i in range(len(nums)):
            if switch == False:
                break
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        output.append(i)
                        output.append(j)
                        switch = False
                        break

        return output
        