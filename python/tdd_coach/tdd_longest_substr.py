import unittest


def longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        print(f"right: {right}, left: {left}, char_set: {char_set}")
        while s[right] in char_set:
            print(f"Removing {s[left]} from char_set {char_set}")
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


class TestLongestSubstring(unittest.TestCase):

    def test_longest(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)
        # self.assertEqual(longest_substring("bbbbb"), 1)
        # self.assertEqual(longest_substring("pwwkew"), 3)
        # self.assertEqual(longest_substring(""), 0)
        # self.assertEqual(longest_substring(" "), 1)
