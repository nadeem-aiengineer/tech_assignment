# 🧠 Software Developer Technical Assignment

Welcome! This repository contains solutions for the two-part technical assignment for the Software Developer role. Each assignment is implemented in Python with clean code, proper abstraction, and unit tests.

---

## 📁 Folder Structure

```
submission/
├── assignment1/
│   ├── threshold_selector.py        # Function to select best classification threshold
│   └── test_threshold_selector.py   # Unit tests for threshold selector
├── assignment2/
│   ├── fsm_mod3.py                  # FSM class + mod-3 binary remainder logic
│   └── test_fsm_mod3.py             # Unit tests for FSM and mod-3 logic
└── README.md
```

---

## 📌 Assignment 1 – Best Threshold Selector

### ✅ Problem
Given binary classification results (`TP`, `FP`, `TN`, `FN`) for different confidence score thresholds, find the best threshold where **recall ≥ 0.9**.

### 🧪 Example Input
```python
threshold_metrics = {
    0.1: {"tp": 96, "fp": 32, "tn": 58, "fn": 4},
    0.2: {"tp": 90, "fp": 24, "tn": 66, "fn": 10},
    ...
}
```

### 🚀 Run the Script
```bash
cd assignment1
python threshold_selector.py
```

### 🧪 Run Unit Tests
```bash
python -m unittest test_threshold_selector.py
```

---

## 📌 Assignment 2 – FSM for Binary Mod-3

### ✅ Problem
Implement a Finite State Machine (FSM) to compute the remainder of a binary string interpreted as an unsigned integer **modulo 3**, **without using `%` or int conversion**.

### 🧠 FSM Details
- States: `S0`, `S1`, `S2` represent remainders `0`, `1`, `2`
- Transitions follow the FSM delta rules as described in the assignment prompt

### 🚀 Run the Script
```bash
cd assignment2
python fsm_mod3.py
```

### 🧪 Run Unit Tests
```bash
python -m unittest test_fsm_mod3.py
```

---

## 🧼 Code Highlights

- ✅ Clean modular code
- ✅ Object-Oriented Design (FSM as a generic class)
- ✅ Full test coverage with edge case handling
- ✅ Clear comments and naming conventions
- ✅ No external dependencies – Python 3 standard library only

---

## 👨‍💻 Environment

- Language: Python 3.x
- No additional libraries required

---

Thank you for reviewing this submission!
