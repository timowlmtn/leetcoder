# LINKED LISTS CHEAT SHEET

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# 1. Reverse Linked List
# “Given the head of a singly linked list, reverse the list in-place and return
# its new head.”
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


# 2. Merge Two Sorted Lists
# “You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list by splicing together
# the nodes of the first two lists. Return the head of the merged linked list.”
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        tail.next = p1 or p2
        return dummy.next


# 3. Intersection of Two Linked Lists
# “Given the heads of two singly linked-lists headA and headB, return the
# node at which the two lists intersect. If they do not intersect, return None.”
class Solution:
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA


# 4. Remove Duplicates from Sorted List
# “Given the head of a sorted linked list, delete all duplicates such that
# each element appears only once. Return the sorted list.”
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# GENERAL TIPS
# • Clarify if it’s a singly or doubly linked list and if in-place modifications
#    are allowed.
# • Discuss pointer manipulation: maintain prev, curr, next references carefully.
# • For intersection, confirm memory constraints and aim for O(m+n) time, O(1) space.
# • State complexities: typically O(n) time, O(1) extra space.
# • Test edge cases: empty list, single node, no intersection, all duplicates.
