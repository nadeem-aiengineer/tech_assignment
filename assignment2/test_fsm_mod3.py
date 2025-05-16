# test_fsm_mod3.py

import unittest
from fsm_mod3 import Mod3FSM


class TestMod3FSM(unittest.TestCase):
    def setUp(self):
        self.fsm = Mod3FSM()

    def test_assignment_examples(self):
        self.assertEqual(self.fsm.get_mod3_remainder("1101"), 1)
        self.assertEqual(self.fsm.get_mod3_remainder("1110"), 2)
        self.assertEqual(self.fsm.get_mod3_remainder("1111"), 0)

    def test_1_to_15_binary_values(self):
        for i in range(1, 16):
            binary = bin(i)[2:]
            expected = i % 3
            with self.subTest(binary=binary):
                self.assertEqual(self.fsm.get_mod3_remainder(binary), expected)

    def test_leading_zeros(self):
        self.assertEqual(self.fsm.get_mod3_remainder("000"), 0)
        self.assertEqual(self.fsm.get_mod3_remainder("0001"), 1)
        self.assertEqual(self.fsm.get_mod3_remainder("0010"), 2)
        self.assertEqual(self.fsm.get_mod3_remainder("000011"), 0)

    def test_all_3_bit_binaries(self):
        for i in range(8):
            binary = format(i, "03b")
            expected = i % 3
            with self.subTest(binary=binary):
                self.assertEqual(self.fsm.get_mod3_remainder(binary), expected)

    def test_all_4_bit_binaries(self):
        for i in range(16):
            binary = format(i, "04b")
            expected = i % 3
            with self.subTest(binary=binary):
                self.assertEqual(self.fsm.get_mod3_remainder(binary), expected)

    def test_long_inputs(self):
        self.assertEqual(self.fsm.get_mod3_remainder("1" * 20), int("1" * 20, 2) % 3)
        self.assertEqual(self.fsm.get_mod3_remainder("10" * 15), int("10" * 15, 2) % 3)
        self.assertEqual(self.fsm.get_mod3_remainder("101" * 10), int("101" * 10, 2) % 3)
        self.assertEqual(self.fsm.get_mod3_remainder("0" * 50), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.fsm.get_mod3_remainder("")
        with self.assertRaises(ValueError):
            self.fsm.get_mod3_remainder("102")
        with self.assertRaises(ValueError):
            self.fsm.get_mod3_remainder("abc")
        with self.assertRaises(ValueError):
            self.fsm.get_mod3_remainder("1.0")

    def test_reset_behavior_between_calls(self):
        self.assertEqual(self.fsm.get_mod3_remainder("1010"), 1)
        self.assertEqual(self.fsm.get_mod3_remainder("1"), 1)
        self.assertEqual(self.fsm.get_mod3_remainder("0"), 0)


if __name__ == "__main__":
    unittest.main()
