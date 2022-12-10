from aoc_utils.parse import parse_multi_element


class CPU:
    def __init__(self):
        self.x = 1
        self.cycle_history = []

    def process_instruction(self, instruction: list):
        if instruction[0] == 'addx':
            # begin
            self.cycle_history.append(self.x)
            # process
            self.cycle_history.append(self.x)
            # write
            self.x += instruction[1]
        elif instruction[0] == 'noop':
            self.cycle_history.append(self.x)

    def get_signal_sum(self, *cycle_steps):
        signal_sum = 0
        for step in cycle_steps:
            current_signal_strength = self.cycle_history[step - 1] * step
            print(current_signal_strength)
            signal_sum += current_signal_strength
        return signal_sum


if __name__ == '__main__':
    cpu = CPU()
    for instruction_line in parse_multi_element('instructions.txt'):
        cpu.process_instruction(instruction_line)
    print(cpu.get_signal_sum(20, 60, 100, 140, 180, 220))
