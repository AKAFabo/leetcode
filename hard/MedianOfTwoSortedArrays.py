class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        merged = sorted(nums1 + nums2)   # you already had the + merge
        n = len(merged)
        mid = n // 2