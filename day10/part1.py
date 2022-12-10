from aoc_utils.parse import parse_multi_element

if __name__ == '__main__':
    cycle = 1
    x = 1
    for instruction in parse_multi_element('instructions.txt'):
        if instruction[0] == 'noop':
            cycle += 1
        if instruction[0] == 'addx':
            value = instruction[1]
            x += 1
            x += value






