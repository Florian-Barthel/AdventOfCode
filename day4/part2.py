from part1 import convert_line


def is_overlapping(start1: int, end1: int, start2: int, end2: int):
    overlap1 = start1 <= start2 and end1 >= start2
    overlap2 = start2 <= start1 and end2 >= start1
    return overlap1 or overlap2


if __name__ == '__main__':
    with open('assignment_pairs.txt') as f:
        overlapping_assignments = 0
        for line in f.read().splitlines():
            start1, end1, start2, end2 = convert_line(line)
            if is_overlapping(start1, end1, start2, end2):
                overlapping_assignments += 1
    print(overlapping_assignments)
