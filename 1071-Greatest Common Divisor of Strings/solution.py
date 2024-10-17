class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcdOfStrings_helper(str1, str2):
            for i in range(len(str1), 0, -1 ):
                for j in range(len(str1)):
                    tmp = str1[j:j + i]
                    if len(tmp) != i:
                        break
                    result_str1 = str1.replace(tmp, "")
                    result_str2 = str2.replace(tmp, "")
                    if result_str1 == result_str2 =="":
                        return tmp
            return ""
        
        if len(str1) <= len(str2):
            return gcdOfStrings_helper(str1, str2)
        else:
            return gcdOfStrings_helper(str2, str1)

# Cool solution
# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         if str1 + str2 != str2 + str1:
#             return ""
#         if len(str1) == len(str2):
#             return str1
#         if len(str1) > len(str2):
#             return self.gcdOfStrings(str1[len(str2):], str2)
#         return self.gcdOfStrings(str1, str2[len(str1):])            
        

solution = Solution()
str1 = "aa"
str2 = "a"

print(solution.gcdOfStrings(str1, str2))

