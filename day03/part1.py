import numpy as np


def get_priority(item: str) -> int:
    assert len(item) == 1
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38
    raise ValueError('The item has to be a single letter.')


def split_rucksack_compartments(rucksack_content: str):
    num_total_items = len(rucksack_content)
    assert num_total_items % 2 == 0
    split_index = num_total_items // 2
    return [rucksack_content[:split_index], rucksack_content[split_index:]]


def get_same_letters(left, right):
    left_ascii_index = np.array(list(map(ord, left)))
    right_ascii_index = np.array(list(map(ord, right)))
    diff = left_ascii_index[None, :] - right_ascii_index[:, None]
    index = np.where(diff == 0)[0]
    duplicate_items = list(set(right_ascii_index[index]))
    return list(map(chr, duplicate_items))


if __name__ == '__main__':
    with open('rucksack_list.txt') as f:
        priority_sum = 0
        for line in f.read().splitlines():
            left_compartment, right_compartment = split_rucksack_compartments(line)
            same_letter = get_same_letters(left_compartment, right_compartment)[0]
            priority_sum += get_priority(same_letter)
    print(priority_sum)
