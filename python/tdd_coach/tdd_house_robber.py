import unittest


def house_robber(nums: list[int]) -> int:
    """
    Given a list of non-negative integers representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight without alerting the police.
    You cannot rob two adjacent houses.
    :param nums:
    :return:
    """

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev = 0
    curr = 0

    for num in nums:
        print(f"prev: {prev}, curr: {curr}, num: {num}")
        # Calculate the maximum amount of money that can be robbed up to the current house
        temp = curr

        curr = max(prev + num, curr)

        prev = temp

    return curr


class TestHouseRobber(unittest.TestCase):

    def test_rob_some(self):
        self.assertEqual(house_robber([2, 7, 9, 3, 1]), 12)
        self.assertEqual(
            house_robber(
                [],
            ),
            0,
        )
        self.assertEqual(house_robber([1, 1000, 1]), 1000)
        self.assertEqual(house_robber([1, 0, 1000]), 1001)
