# HASH TABLES (MAPS/SETS) CHEAT SHEET

from typing import List
from collections import defaultdict


# 1. Two Sum
# “Given an array of integers ‘nums’ and an integer ‘target’, return the indices
# of the two numbers such that they add up to ‘target’. Assume exactly one solution
# and you may not use the same element twice. Return the answer in any order.”
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []


# 2. Contains Duplicate
# “Given an integer array ‘nums’, return True if any value appears at least
# twice in the array, and False if every element is distinct.”
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# 3. Group Anagrams
# “Given an array of strings ‘strs’, group the anagrams together. You may return
# the answer in any order.”
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, List[str]] = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


# 4. Happy Number
# “Write an algorithm to determine if a number ‘n’ is happy. A happy number
# eventually reaches 1 when replaced by the sum of the squares of its digits.
# Return True if ‘n’ is a happy number, otherwise False.”
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x: int) -> int:
            total = 0
            while x:
                x, d = divmod(x, 10)
                total += d * d
            return total

        seen: set[int] = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# GENERAL TIPS
# • Confirm expected input sizes to discuss hash table sizing or collision handling.
# • State complexities: typically O(n) time and O(n) space.
# • For grouping keys, discuss trade-offs between sorted-string keys vs. character-count tuples.
# • Clarify how Python’s built-in dict handles collisions; for custom implementations note chaining vs. open addressing.
