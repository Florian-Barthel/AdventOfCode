from part1 import CraneDoc

if __name__ == '__main__':
    crane_doc = CraneDoc('crane.txt')
    found_start = False
    with open('crane.txt') as f:
        for line in f.read().splitlines():
            if found_start:
                _, amount, _, from_index, _, to_index = line.split()
                crane_doc.move_multiple(int(from_index), int(to_index), int(amount))
            if line == '':
                found_start = True

    crane_doc.print_top()
