class Solution():
    def isPowerOfFour(self, n):
        while n >= 4:
            n /= 4
        if n == 1:
            return True
        else:
            return False