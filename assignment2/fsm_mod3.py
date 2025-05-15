# fsm_mod3.py
# A finite state machine to calculate binary % 3 without using modulus or int()

class FSM:
    def __init__(self, states, input_symbols, initial_state, final_states, transition_function):
        self.states = states
        self.input_symbols = input_symbols
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.initial_state

    def transition(self, symbol: str):
        if symbol not in self.input_symbols:
            raise ValueError(f"Invalid symbol '{symbol}' in input.")
        self.current_state = self.transition_function[self.current_state][symbol]

    def process(self, input_sequence: str):
        self.reset()
        for symbol in input_sequence:
            self.transition(symbol)
        return self.current_state


def mod3_fsm():
    # Define states and transitions for mod-3 FSM
    states = {"S0", "S1", "S2"}
    input_symbols = {"0", "1"}
    initial_state = "S0"
    final_states = {"S0", "S1", "S2"}
    transitions = {
        "S0": {"0": "S0", "1": "S1"},
        "S1": {"0": "S2", "1": "S0"},
        "S2": {"0": "S1", "1": "S2"},
    }

    return FSM(states, input_symbols, initial_state, final_states, transitions)


def binary_mod3(binary_str: str) -> int:
    """
    Processes a binary string to compute binary value % 3 using FSM.

    Args:
        binary_str: A string of 0s and 1s.

    Returns:
        The remainder after division by 3.
    """
    state_to_remainder = {"S0": 0, "S1": 1, "S2": 2}
    fsm = mod3_fsm()
    final_state = fsm.process(binary_str)
    return state_to_remainder[final_state]


# Sample usage
if __name__ == "__main__":
    samples = ["1101", "1111", "1010", "000", "1", "11"]
    for binary in samples:
        print(f"{binary} -> {binary_mod3(binary)}")
