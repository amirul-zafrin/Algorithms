from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}

        for num in nums:
            if num in check:
                return True
            check[num] = 1

        return False
