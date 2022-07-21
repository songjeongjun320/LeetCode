class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        sum = 0 # 삼중 포문 안에서 더하는 값을 저장할 변수 / 마지막에는 target이 되는 변수
        output = []
        s = set()
        two_d_list = [0,0,0] # i j k 의 값을 저장할 리스트

        ## 제시된 nums의 모든 three sum 경우의 수 판별, 그 중 중복된 sum값 찾아냄.
        for i in range(len(nums)):
            if i+1 >= len(nums):
                continue
            sum = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    tmp = []
                    tmp.append(nums[i])
                    tmp.append(nums[j])
                    tmp.append(nums[k])
                    tmp.sort()
                    if tuple(tmp) not in s:
                        s.add(tuple(tmp))
                        output.append(tmp)
                    j += 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1   
        return output