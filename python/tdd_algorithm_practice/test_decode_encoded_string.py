import unittest


def decode_string(string_in: str) -> str:
    result = ""
    letter_counter = []
    count = 0
    for char_at in string_in:
        if char_at.isdigit():
            if len(letter_counter) == count:
                letter_counter.append(char_at)
        else:
            for i in range(int(letter_counter[count])):
                result += char_at
            count += 1

    return result


class TestDecodeEncodedString(unittest.TestCase):
    def test_decode_string(self):
        self.assertEqual(decode_string("4A3B2C1D2A"), "AAAABBBCCDAA")
