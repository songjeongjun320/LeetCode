class Solution(object):
    def isAnagram(self, s, t):
        list_s = []
        list_t = []
        if len(s) != len(t):
            return False
        for _ in range(len(s)):
            list_s.append(s[_])
            list_t.append(t[_])
        list_s.sort()
        list_t.sort()
        if list_s == list_t:
            return True
        else:
            return False