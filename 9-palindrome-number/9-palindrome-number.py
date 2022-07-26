class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        left = 0
        right = len(x)-1
        switch = True

        while left < right:
            if x[left] != x[right]:
                switch = False
                break
            left += 1
            right -= 1

        return switch