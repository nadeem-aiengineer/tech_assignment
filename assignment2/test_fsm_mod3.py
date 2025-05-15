import unittest
from fsm_mod3 import binary_mod3

class TestFSMMod3(unittest.TestCase):

    def test_correct_outputs(self):
        test_cases = {
            "0": 0,
            "1": 1,
            "10": 2,
            "11": 0,
            "110": 0,
            "111": 1,
            "1101": 1,
            "1110": 2,
            "1111": 0,
            "000": 0
        }

        for binary_str, expected in test_cases.items():
            self.assertEqual(binary_mod3(binary_str), expected, f"Failed for input: {binary_str}")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            binary_mod3("12001")

    def test_empty_input(self):
        # Empty string returns initial state S0 -> remainder 0
        self.assertEqual(binary_mod3(""), 0)

    def test_long_binary_input(self):
        binary_str = "1010101010101010101010101010101010101010101010101010"  # 52 bits
        # Just ensuring it does not raise error
        result = binary_mod3(binary_str)
        self.assertIn(result, [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
