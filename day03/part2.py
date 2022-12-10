
from part1 import get_same_letters, get_priority


if __name__ == '__main__':
    with open('rucksack_list.txt') as f:
        priority_sum = 0
        lines = f.read().splitlines()
        for i in range(0, len(lines), 3):
            rucksack1, rucksack2, rucksack3 = lines[i:i+3]
            same_letters_1_2 = get_same_letters(rucksack1, rucksack2)
            same_letters_2_3 = get_same_letters(rucksack2, rucksack3)
            total_same_letters = get_same_letters(same_letters_1_2, same_letters_2_3)
            priority_sum += get_priority(total_same_letters[0])
    print(priority_sum)
