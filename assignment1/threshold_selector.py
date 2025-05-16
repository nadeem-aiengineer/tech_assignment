import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)


class ThresholdSelector:
    def __init__(self, metrics: Dict[float, Dict[str, int]]):
        """
        Initialize with a dictionary of thresholds and associated metrics.
        Each value must contain keys: 'tp', 'fp', 'tn', 'fn'.
        """
        self.metrics = metrics
        self.max_value = None

    @staticmethod
    def calculate_recall(tp: int, fn: int) -> float:
        """
        Calculate recall: TP / (TP + FN)
        """
        if tp + fn == 0:
            logger.warning("Both TP and FN are zero — recall is set to 0.")
            return 0.0
        return tp / (tp + fn)

    def get_best_threshold(self, min_recall: float = 0.9) -> Optional[float]:
        """
        Returns the highest threshold with recall >= min_recall.
        If none found, returns None.
        """
        valid_thresholds = []

        for threshold, stats in self.metrics.items():
            tp = stats.get("tp", 0)
            fn = stats.get("fn", 0)
            recall = self.calculate_recall(tp, fn)

            logger.debug(f"Threshold: {threshold} — TP: {tp}, FN: {fn}, Recall: {recall:.4f}")

            if recall >= min_recall:
                valid_thresholds.append(threshold)
                logger.info(f"Threshold {threshold} accepted with recall {recall:.4f}")

        if valid_thresholds:
            self.max_value = max(valid_thresholds, default=valid_thresholds[0])
            logger.info(f"Best threshold with recall ≥ {min_recall}: {self.max_value}")
        else:
            self.max_value = None
            logger.warning("No threshold met the recall requirement.")

        return self.max_value


def main():
    # Example usage
    threshold_data = {
        0.1: {"tp": 95, "fp": 10, "tn": 90, "fn": 5},
        0.2: {"tp": 85, "fp": 12, "tn": 88, "fn": 15},
        0.3: {"tp": 92, "fp": 8, "tn": 92, "fn": 8},
        0.4: {"tp": 80, "fp": 7, "tn": 95, "fn": 20},
        0.5: {"tp": 90, "fp": 6, "tn": 94, "fn": 10},
        0.6: {"tp": 93, "fp": 5, "tn": 96, "fn": 7},
        0.7: {"tp": 70, "fp": 4, "tn": 97, "fn": 30},
        0.8: {"tp": 91, "fp": 3, "tn": 98, "fn": 9},
        0.9: {"tp": 85, "fp": 2, "tn": 99, "fn": 15}
    }

    selector = ThresholdSelector(threshold_data)
    best = selector.get_best_threshold()

    if best is not None:
        logger.info(f"Best threshold with recall >= 0.9 is: {best}")
    else:
        logger.info("No threshold meets the recall requirement.")


if __name__ == "__main__":
    main()
