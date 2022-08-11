"""
Given an integer array instructions, you are asked to create a sorted 
array from the elements in instructions. You start with an empty container 
nums. For each element from left to right in instructions, insert it into 
nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion 
is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums 
will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. 
Since the answer may be large, return it modulo 109 + 7
"""

# https://leetcode.com/problems/create-sorted-array-through-instructions/


class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        d = {}
        for i in range(len(instructions)):
            if instructions[i] in d:
                d[instructions[i]] += 1
            else:
                d[instructions[i]] = 1
        cost = 0
        for key in d:
            cost += min(d[key], d[key-1])
        return cost % (10**9 + 7)
