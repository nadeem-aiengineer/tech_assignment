# Software Developer Technical Assignment

# Threshold Selector & Mod-3 FSM

This project includes two separate Python-based assignments that demonstrate object-oriented design, proper software structure, and automated testing using `unittest` and `pytest`.

## Project Layout

Each assignment is located in its own folder for clarity and modularity.

```
SUBMISSION/
├── assignment1/
│   ├── threshold_selector.py
│   └── test_threshold_selector.py
│
├── assignment2/
│   ├── fsm_mod3.py
│   └── test_fsm_mod3.py
│
├── requirements.txt
└── README.md
```

## Assignment 1: Threshold Selector

### Problem
Given binary classification results (`TP`, `FP`, `TN`, `FN`) for different confidence score thresholds, find the best threshold where **recall ≥ 0.9**.

### What it does:
- Computes recall for each threshold using TP and FN values
- Selects the highest threshold that meets the recall criteria
- Includes logging for traceability and a test suite that handles various scenarios

### Example Input
```python
threshold_metrics = {
    0.1: {"tp": 96, "fp": 32, "tn": 58, "fn": 4},
    0.2: {"tp": 90, "fp": 24, "tn": 66, "fn": 10},
    ...
}
```

### How to run:
```bash
cd assignment1
python threshold_selector.py
```

### How to test:
```bash
pytest
```

You can also use the built-in unittest runner:
```bash
python -m unittest test_threshold_selector.py -v
```

## Assignment 2: Mod-3 Finite State Machine

### Problem
Implement a Finite State Machine (FSM) to compute the remainder of a binary string interpreted as an unsigned integer **modulo 3**, **without using `%` or int conversion**.

### Key concepts:
- Uses three states (S0, S1, S2) representing remainders 0, 1, 2
- Defines transitions for each bit input ('0' or '1')
- The final state determines the remainder (0, 1, or 2)
- Transitions follow the FSM delta rules as described in the assignment prompt

### How to run:
```bash
cd assignment2
python fsm_mod3.py
```

### How to test:
```bash
pytest
```

Or using unittest directly:
```bash
python -m unittest test_fsm_mod3.py -v
```

## Code Highlights
- Clean modular code
- Object-Oriented Design (FSM as a generic class)
- Full test coverage with edge case handling
- Clear comments and naming conventions
- No external dependencies – Python 3 standard library only

## Requirements

This project only requires Python and `pytest` to run and test.

```
pytest>=7.0
```

Install with:

```bash
pip install -r requirements.txt
```

## Final Notes

This repository was designed with readability and reusability in mind. The codebase adheres to Python best practices including modularization, meaningful naming, defensive programming, and full test coverage.
