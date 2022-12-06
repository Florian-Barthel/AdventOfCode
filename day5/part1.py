import re


class CraneDoc:
    def __init__(self, filename):
        self.num_elements = None
        self.current_state = self.get_current_state(filename)

    def get_current_state(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()
            self.num_elements = len(lines[0]) // 4 + 1
            current_state = [[] for _ in range(self.num_elements)]
            for line in lines:
                if line == '':
                    return current_state
                split_row = [line[i*4:i*4+4] for i in range(self.num_elements)]
                for index, element in enumerate(split_row):
                    m = re.search(r'[\w+]', element)
                    if m is not None:
                        current_state[index].append(m.group(0))

    def move_single(self, start, target):
        start_index = start - 1
        target_index = target - 1
        # index out of range
        if start_index >= self.num_elements or target_index >= self.num_elements:
            return
        # list empty
        if len(self.current_state[start_index]) < 1:
            return
        element = self.current_state[start_index].pop(0)
        self.current_state[target_index].insert(0, element)

    def move_multiple(self, start, target, amount):
        start_index = start - 1
        target_index = target - 1
        # index out of range
        if start_index >= self.num_elements or target_index >= self.num_elements:
            return

        for i in range(amount):
            # list empty
            if len(self.current_state[start_index]) < 1:
                return

            element = self.current_state[start_index].pop(0)
            self.current_state[target_index].insert(i, element)

    def print_top(self):
        for stack in self.current_state:
            print(stack[0], end='')


if __name__ == '__main__':
    crane_doc = CraneDoc('crane.txt')
    found_start = False
    with open('crane.txt') as f:
        for line in f.read().splitlines():
            if found_start:
                _, amount, _, from_index, _, to_index = line.split()
                for _ in range(int(amount)):
                    crane_doc.move(int(from_index), int(to_index))
            if line == '':
                found_start = True

    crane_doc.print_top()

