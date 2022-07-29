class Solution(object):
    def strStr(self, haystack, needle):
        for _ in range(len(haystack)):
            if not needle in haystack:
                return -1
        return haystack.index(needle)