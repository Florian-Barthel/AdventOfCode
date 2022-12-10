

def is_fully_overlapping(start1: int, end1: int, start2: int, end2: int):
    elf1_overlaps_elf2 = start1 >= start2 and end1 <= end2
    elf2_overlaps_elf1 = start2 >= start1 and end2 <= end1
    return elf2_overlaps_elf1 or elf1_overlaps_elf2


def convert_line(line_of_pairs: str):
    elf1, elf2 = line_of_pairs.split(',')
    start1, end1 = list(map(int, elf1.split('-')))
    start2, end2 = list(map(int, elf2.split('-')))
    return start1, end1, start2, end2


if __name__ == '__main__':
    with open('assignment_pairs.txt') as f:
        fully_overlapping_assignments = 0
        for line in f.read().splitlines():
            start1, end1, start2, end2 = convert_line(line)
            if is_fully_overlapping(start1, end1, start2, end2):
                fully_overlapping_assignments += 1
    print(fully_overlapping_assignments)
