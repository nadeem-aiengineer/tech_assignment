
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

This module helps determine the best threshold from a list of binary classification metrics where the recall is at least 0.9.

### What it does:

- Computes recall for each threshold using TP and FN values
- Selects the highest threshold that meets the recall criteria
- Includes logging for traceability and a test suite that handles various scenarios

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

This FSM implementation takes a binary string input and simulates transitions between states to determine the remainder when the binary value is divided by 3.

### Key concepts:

- Uses three states (S0, S1, S2)
- Defines transitions for each bit input ('0' or '1')
- The final state determines the remainder (0, 1, or 2)

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

## Testing

All logic in both assignments is covered with detailed unit tests, including edge cases, invalid input handling, and reset behavior between test cases.

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
