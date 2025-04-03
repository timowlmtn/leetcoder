import unittest


def double_even_int(array_of_int) -> list:
    """
    Given an array of integers, double the even integers and leave the odd integers unchanged.

    :param array_of_int:
    :return:
    """
    idx = 0
    for int_val in array_of_int:
        if int_val % 2 != 0:
            array_of_int[idx] = int_val
        else:
            array_of_int[idx] = int_val * 2
        idx += 1

    return array_of_int


class TestDoubleEvenInt(unittest.TestCase):

    def test_double_even_int(self):
        self.assertEqual(double_even_int([1, 2, 3]), [1, 4, 3])
