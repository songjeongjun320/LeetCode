class Solution(object):       
    def generateParenthesis(self, n):
        def generate(l, r, tmp):
            if (r == 0):
                return tmp
            if (l >= r):
                tmp = tmp + "("
                l -= 1
                return generate(l, r, tmp)
            tmp = tmp + ")"
            r -= 1
            return generate(l, r, tmp)
        
        l, r = n, n
        output = []
        for l in range(l,0,-1):
            tmp = ""
            tmp += l * "("
            tmp += ")"        
            output.append(generate(n - l, n - 1, tmp)) # 0, 2, ((()

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