import unittest
from threshold_selector import best_threshold

class TestThresholdSelector(unittest.TestCase):

    def test_best_threshold_found(self):
        metrics = {
            0.1: {"tp": 95, "fp": 30, "tn": 60, "fn": 5},   # Recall = 0.95
            0.2: {"tp": 90, "fp": 20, "tn": 70, "fn": 10},  # Recall = 0.9
            0.3: {"tp": 70, "fp": 10, "tn": 80, "fn": 30}   # Recall = 0.7
        }
        result = best_threshold(metrics)
        self.assertEqual(result, (0.1, 0.95))

    def test_no_valid_threshold(self):
        metrics = {
            0.1: {"tp": 40, "fp": 30, "tn": 60, "fn": 60},  # Recall = 0.4
            0.2: {"tp": 50, "fp": 25, "tn": 65, "fn": 50}   # Recall = 0.5
        }
        result = best_threshold(metrics)
        self.assertIsNone(result)

    def test_empty_input(self):
        result = best_threshold({})
        self.assertIsNone(result)

    def test_missing_keys(self):
        with self.assertRaises(KeyError):
            metrics = {
                0.1: {"tp": 40, "fp": 20, "tn": 30}  # Missing 'fn'
            }
            best_threshold(metrics)

if __name__ == '__main__':
    unittest.main()
