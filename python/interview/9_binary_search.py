# BINARY SEARCH CHEAT SHEET

# 1. Classic Binary Search
# Description: search for target in sorted list by halving the search range.


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# 2. Search Insert Position
# Description: find the index where target should be inserted to maintain order.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


# 3. First Bad Version
# Description: use binary search to locate the first version where isBadVersion is True.


# The isBadVersion API is defined for you:
def isBadVersion(version: int) -> bool:
    if version == 2:
        return True
    else:
        return False  # Placeholder for actual implementation


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# GENERAL TIPS
# - Always confirm the input is sorted and clarify how duplicates should be handled.
# - Choose loop bounds carefully: use `<=` when you need to check equality inside, `<` when narrowing down a range.
# - Avoid overflow in mid calculation: mid = left + (right - left) // 2.
# - State complexities: O(log n) time, O(1) extra space.
# - Test edge cases: empty array, single element, target at ends, target not present.
