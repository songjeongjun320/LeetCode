
class Solution(object):
    def isValid(self, s):
        if not s:
            return False
        if len(s)%2 != 0:
            return False
        check_string = []
        for _ in range(len(s)):
            if s[_] == '(' or s[_] == '{' or s[_] == '[':
                check_string.append(s[_])
            else:
                if not check_string:
                    return False
                if s[_] == ')':
                    if check_string[len(check_string)-1] != '(':
                        return False
                    else:
                        check_string.pop(len(check_string)-1)
                elif s[_] == '}':
                    if check_string[len(check_string)-1] != '{':
                        return False
                    else:
                        check_string.pop(len(check_string)-1)
                elif s[_] == ']':
                    if check_string[len(check_string)-1] != '[':
                        return False
                    else:
                        check_string.pop(len(check_string)-1)
        if check_string:
            return False

        return True