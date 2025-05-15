# threshold_selector.py
# This script finds the best classification threshold that gives recall >= 0.9

from typing import Dict, Tuple, Optional

def calculate_recall(tp: int, fn: int) -> float:
    """
    Calculate recall: TP / (TP + FN)
    """
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0

def best_threshold(metrics: Dict[float, Dict[str, int]]) -> Optional[Tuple[float, float]]:
    """
    Returns the best threshold (with highest recall >= 0.9).
    
    Args:
        metrics: A dictionary where the key is the threshold (float),
                 and the value is another dictionary containing 'tp', 'fp', 'tn', 'fn'.
                 
    Returns:
        A tuple of (threshold, recall) if valid threshold found, else None.
    """
    valid_thresholds = []

    for threshold, stats in metrics.items():
        recall = calculate_recall(stats['tp'], stats['fn'])
        if recall >= 0.9:
            valid_thresholds.append((threshold, recall))

    # Return the threshold with the highest recall among valid ones
    return max(valid_thresholds, key=lambda x: x[1]) if valid_thresholds else None


# Sample usage
if __name__ == "__main__":
    threshold_metrics = {
        0.1: {"tp": 96, "fp": 32, "tn": 58, "fn": 4},
        0.2: {"tp": 90, "fp": 24, "tn": 66, "fn": 10},
        0.3: {"tp": 82, "fp": 18, "tn": 72, "fn": 18},
        0.4: {"tp": 75, "fp": 12, "tn": 78, "fn": 25},
        0.5: {"tp": 60, "fp": 8, "tn": 82, "fn": 40}
    }

    result = best_threshold(threshold_metrics)
    if result:
        print(f"Best threshold with recall ≥ 0.9: {result[0]} (Recall: {result[1]:.2f})")
    else:
        print("No threshold found with recall ≥ 0.9.")
