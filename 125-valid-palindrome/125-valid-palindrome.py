class Solution():
    def isPalindrome(self, s):
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        print(s)
        for _ in range(len(s)):
            if s[_] != s[len(s)-_-1]:
                return False
        return True