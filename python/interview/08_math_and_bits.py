# MATH & BIT-MANIPULATION CHEAT SHEET

# 1. Reverse Integer
# Description: Reverse digits of an integer and handle 32-bit signed overflow.


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        while x_abs:
            rev = rev * 10 + x_abs % 10
            x_abs //= 10
        rev *= sign
        return rev if -(2**31) <= rev <= 2**31 - 1 else 0


# 2. Palindrome Number
# Description: Check if an integer reads the same forward and backward.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]


# 3. Number of 1 Bits
# Description: Count the number of set bits in an unsigned integer.


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


# 4. Power of Two
# Description: Determine if a number is a power of two using a bit trick.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


# GENERAL TIPS
# - Know integer limits and check for overflow when reversing digits.
# - Use bitwise operators (&, |, ^, ~, <<, >>) for O(1) operations.
# - Explain bit tricks: n & (n - 1) unsets the lowest set bit.
# - State complexities: typically O(log n) time, O(1) space.
# - Consider edge cases: x=0, negatives, maximum values.
