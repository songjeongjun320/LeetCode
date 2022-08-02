class Solution():
    def plusOne(self, digits):
        digits.reverse()
        r = 1
        for _ in range(len(digits)):
            digits[_] = digits[_] + r
            r = 0
            if digits[_] == 10:
                digits[_] = 0
                r = 1
        if r == 1:
            digits.append(1)
        digits.reverse()
        return digits