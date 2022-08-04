class Solution():
    def climbStairs(self, n):
        if n == 1:
            return 1
        tmp = []
        count = 0
        for x in range(n+1):
            y = int((n-x)/2)
            if n == x + 2*y:
                tmp.append([x,y])

        for _ in range(len(tmp)):
            count += int(factorial(tmp[_][0]+tmp[_][1])/(factorial(tmp[_][0])*factorial(tmp[_][1])))
        return count