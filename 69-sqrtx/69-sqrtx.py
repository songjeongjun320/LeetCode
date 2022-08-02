class Solution():
    def mySqrt(self, x):
        _ = 0
        left = 0
        right = 0
        while True:
            left = _*_
            right = (_+1)*(_+1)
            if x >= left and x < right:
                return _
            _ += 1
    