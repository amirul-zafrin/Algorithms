from typing import List


class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # return sorted(nums1[:m] + nums2[:n])
        nums1[m:] = nums2[:n]
        return nums1.sort()
