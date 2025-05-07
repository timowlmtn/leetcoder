# ARRAYS & STRINGS CHEAT SHEET

from typing import List


# 1. Two Sum
# “Given an array of integers ‘nums’ and an integer ‘target’, return the indices
# of the two numbers such that they add up to ‘target’. Assume exactly one
# solution and you may not use the same element twice.”
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []


# 2. Remove Duplicates from Sorted Array
# “Given a sorted array ‘nums’, remove the duplicates in-place such that
# each element appears only once and return the new length of the array.”
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write


# 3. Valid Anagram
# “Given two strings ‘s’ and ‘t’, return True if ‘t’ is an anagram of ‘s’,
# and False otherwise.”
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# 4. Plus One
# “Given a non-empty array of digits representing a non-negative integer,
# increment one to the integer. The digits are stored such that the most significant digit is at the head of the list.”
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# GENERAL TIPS
# • Clarify whether the input is sorted and if in-place modifications are required.
# • For counting problems, discuss hash map vs sorting trade-offs (O(n) vs O(n log n)).
# • State time/space complexities for each method, and mention any space optimizations.
# • Always test edge cases: empty array/string, single element, all duplicates, carry-over in Plus One.
