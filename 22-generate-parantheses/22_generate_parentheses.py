class Solution(object):
    def generateParenthesis(self, n):
        r, l = 0, 0
        tmp = []
        output = []
        def generateParenthesis_helper(l, r):
            if r == l == n:
                output.append("".join(tmp))
                return
            if l < n:
                tmp.append("(")
                generateParenthesis_helper(l + 1, r)
                tmp.pop()
            if r < l:
                tmp.append(")")
                generateParenthesis_helper(l, r + 1)
                tmp.pop()
        generateParenthesis_helper(0,0)
        return output


solution = Solution()
print(solution.generateParenthesis(3))





# Someone's answer
# class Solution(object):       
    # def generateParenthesis(self, n):
    #     tmp = []
    #     output = []

    #     def backtrack(l, r):
    #         if l == r == n:
    #             output.append("".join(tmp))
    #             return
    #         if l < n:
    #             tmp.append("(")
    #             backtrack(l + 1, r)
    #             tmp.pop()
    #         if r < l:
    #             tmp.append(")")
    #             backtrack(l, r + 1)
    #             tmp.pop()
            
    #     backtrack(0,0)
    #     return output