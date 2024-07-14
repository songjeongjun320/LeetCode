class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def divide(str1, str2):
            result = ""
            for i in range(len(str1) - len(str2) + 1):
                if str1[i:i+len(str2)] == str2:
                    result = str1[0:i] + str1[i+len(str2):len(str1)]
                    break
            return result
        if len(str1) >= len(str2):
            return divide(str1, str2)
        else:
            return divide(str2, str1)
        

solution = Solution()
print(solution.gcdOfStrings("ABCDEF", "ABC"))


        