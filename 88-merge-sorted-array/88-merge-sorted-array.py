class Solution():
    def merge(self, nums1, m, nums2, n):
        for _ in range(len(nums2)):
            nums1.append(nums2[_])
        nums1.sort()
        while len(nums1) != m+n:
            nums1.remove(0)
        return nums1
