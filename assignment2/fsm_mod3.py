# fsm_mod3.py

from typing import Dict


class FSM:
    def __init__(self, states: set, alphabet: set, initial_state: str, transition_function: Dict[str, Dict[str, str]]):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.transition_function = transition_function
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.initial_state

    def transition(self, symbol: str):
        if symbol not in self.alphabet:
            raise ValueError(f"Invalid input symbol: {symbol}")
        self.current_state = self.transition_function[self.current_state][symbol]

    def process(self, input_string: str) -> str:
        self.reset()
        for symbol in input_string:
            self.transition(symbol)
        return self.current_state


class Mod3FSM(FSM):
    def __init__(self):
        states = {"S0", "S1", "S2"}
        alphabet = {"0", "1"}
        initial_state = "S0"
        transition_function = {
            "S0": {"0": "S0", "1": "S1"},
            "S1": {"0": "S2", "1": "S0"},
            "S2": {"0": "S1", "1": "S2"},
        }
        super().__init__(states, alphabet, initial_state, transition_function)
        self.state_to_remainder = {"S0": 0, "S1": 1, "S2": 2}

    def get_mod3_remainder(self, binary_input: str) -> int:
        if not binary_input:
            raise ValueError("Input string cannot be empty.")
        final_state = self.process(binary_input)
        return self.state_to_remainder[final_state]


def main():
    fsm = Mod3FSM()
    examples = ["1101", "1110", "1111", "0", "1", "10", "100", "1010"]

    for binary in examples:
        remainder = fsm.get_mod3_remainder(binary)
        print(f"Input: {binary} → Remainder: {remainder}")


if __name__ == "__main__":
    main()
