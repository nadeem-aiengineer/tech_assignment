import unittest
import logging
from threshold_selector import ThresholdSelector

# Configure logging for test output
logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for more detailed output
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class TestThresholdSelector(unittest.TestCase):

    def setUp(self):
        logger.info(f"----- Running test: {self._testMethodName} -----")

    def test_single_valid_threshold(self):
        data = {
            0.1: {"tp": 50, "fp": 5, "tn": 90, "fn": 50},
            0.3: {"tp": 90, "fp": 6, "tn": 91, "fn": 10}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 0.3)

    def test_multiple_valid_thresholds_returns_highest(self):
        data = {
            0.1: {"tp": 90, "fp": 5, "tn": 90, "fn": 10},
            0.3: {"tp": 93, "fp": 6, "tn": 91, "fn": 7},
            0.5: {"tp": 95, "fp": 4, "tn": 92, "fn": 5}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 0.5)

    def test_none_meets_threshold(self):
        data = {
            0.1: {"tp": 30, "fp": 10, "tn": 80, "fn": 70},
            0.2: {"tp": 20, "fp": 5, "tn": 85, "fn": 80}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertIsNone(result)

    def test_all_thresholds_meet_requirement(self):
        data = {
            0.1: {"tp": 90, "fp": 10, "tn": 90, "fn": 5},
            0.5: {"tp": 91, "fp": 5, "tn": 94, "fn": 4},
            0.9: {"tp": 92, "fp": 3, "tn": 95, "fn": 3}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 0.9)

    def test_empty_input(self):
        selector = ThresholdSelector({})
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertIsNone(result)

    def test_missing_tp_or_fn_defaults_to_zero(self):
        data = {
            0.1: {"fp": 5, "tn": 90, "fn": 5},
            0.2: {"tp": 90, "fp": 5, "tn": 90}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 0.2)

    def test_zero_division_safety(self):
        data = {
            0.1: {"tp": 0, "fp": 5, "tn": 90, "fn": 0},
            0.2: {"tp": 10, "fp": 5, "tn": 90, "fn": 90}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertIsNone(result)

    def test_custom_min_recall_parameter(self):
        data = {
            0.1: {"tp": 80, "fp": 10, "tn": 90, "fn": 20},
            0.2: {"tp": 85, "fp": 12, "tn": 88, "fn": 15}
        }
        selector = ThresholdSelector(data)
        result_85 = selector.get_best_threshold(min_recall=0.85)
        result_80 = selector.get_best_threshold(min_recall=0.80)
        logger.info(f"Result (0.85): {result_85}, Result (0.80): {result_80}")
        self.assertEqual(result_85, 0.2)
        self.assertEqual(result_80, 0.2)

    def test_tied_thresholds_same_value(self):
        data = {
            0.1: {"tp": 90, "fp": 5, "tn": 85, "fn": 10},
            0.5: {"tp": 90, "fp": 4, "tn": 86, "fn": 10}
        }
        selector = ThresholdSelector(data)
        result = selector.get_best_threshold()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 0.5)


if __name__ == "__main__":
    unittest.main()
