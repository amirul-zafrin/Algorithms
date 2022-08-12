class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []

        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.remove(num)

        return res
