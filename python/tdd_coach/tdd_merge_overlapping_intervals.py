import unittest

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlap
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


class TestMergeIntervals(unittest.TestCase):

    def test_merge_intervals(self):
        # A generic for many merge intervals
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

        # Simpler version.
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])

        # No overlap with empty intervals
        self.assertEqual(merge_intervals([]), [])

        # No overlap
        self.assertEqual(
            merge_intervals([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]]
        )
