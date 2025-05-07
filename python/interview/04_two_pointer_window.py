# TWO-POINTER & SLIDING-WINDOW CHEAT SHEET

from typing import List


# 1. Remove Element
# “Given an array of integers ‘nums’ and an integer ‘val’, remove all occurrences of ‘val’ in-place
# and return the new length of the array. The relative order of the remaining elements may be changed.”
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# 2. Valid Palindrome
# “Given a string ‘s’, determine whether it reads the same forward and backward,
# considering only alphanumeric characters and ignoring cases. Return True if it is a palindrome.”
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# 3. Maximum Average Subarray I
# “Given an array of integers and an integer k, find the contiguous subarray of length k
# that has the maximum average value and return this maximum average.”
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k


# 4. Two Sum II - Input Array Is Sorted
# “Given a 1-indexed sorted array ‘numbers’ and a target value, return the indices of the two numbers
# that add up to the target. Assume exactly one solution exists and you may not use the same element twice.”
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]
            if curr < target:
                left += 1
            else:
                right -= 1
