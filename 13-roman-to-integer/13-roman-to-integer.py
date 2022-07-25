class Solution(object):
    def romanToInt(self, s):
        roman_to_int = []
        output = 0

        for _ in range(len(s)):
            if s[_] == 'I':
                roman_to_int.append(1)
            elif s[_] == 'V':
                roman_to_int.append(5)
            elif s[_] == 'X':
                roman_to_int.append(10)
            elif s[_] == 'L':
                roman_to_int.append(50)
            elif s[_] == 'C':
                roman_to_int.append(100)
            elif s[_] == 'D':
                roman_to_int.append(500)
            elif s[_] == 'M':
                roman_to_int.append(1000)

        roman_to_int.append(0)
        _ = 0

        while _ < len(roman_to_int) - 1:
            if roman_to_int[_] >= roman_to_int[_+1]:
                output += roman_to_int[_]
            elif roman_to_int[_] < roman_to_int[_+1]:
                output = output + roman_to_int[_+1] - roman_to_int[_]
                _ += 1
            _ += 1

        return output