class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        output_list = []
        output = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in output_list:
                output_list.append(s[r])
                output = max(output, r - l + 1)
            else:
                output = max(output, r - l)
                output_list.clear()
                l = l + 1
                r = l
                continue
            r += 1                    

        return output   