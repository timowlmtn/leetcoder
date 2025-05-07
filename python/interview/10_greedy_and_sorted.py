# GREEDY & SORTING CHEAT SHEET

# 1. Assign Cookies
# Description: sort children’s greed factors and cookie sizes, then greedily assign smallest sufficient cookie to each child.


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = res = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res


# 2. Lemonade Change
# Description: track counts of $5 and $10 bills to make change for each $20 bill greedily.


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# 3. Merge Sorted Array
# Description: merge nums2 into nums1 in-place by filling from the end.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# 4. Sort Array By Parity
# Description: use two-pointer swap to move even numbers to the front and odd to the back.


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 and not A[j] % 2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A


# GENERAL TIPS
# - Clarify whether the input is already sorted or if you need to sort it (sorting costs O(n log n)).
# - For greedy: explain why a local optimal choice leads to a global optimum.
# - Always discuss time/space complexity up front.
# - Check edge cases: empty lists, minimal sizes.
# - Mention trade-offs: built-in sort vs custom sort, extra data structures vs in-place.```
