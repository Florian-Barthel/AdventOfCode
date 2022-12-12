from part1 import Monkey
import math


if __name__ == '__main__':
    monkey_list = []
    num_rounds = 10000
    verbose = False

    with open('monkeys.txt') as f:
        for monkey_text in f.read().split('\n\n'):
            monkey_list.append(Monkey.from_text(monkey_text))

    prev_lcm = monkey_list[0].test_number
    for i in range(1, len(monkey_list)):
        current_test_number = monkey_list[i].test_number
        prev_lcm = abs(prev_lcm * current_test_number) // math.gcd(prev_lcm, current_test_number)

    for i in range(num_rounds):
        if verbose:
            print('Round', i)
            for monkey in monkey_list:
                print('Monkey', monkey.monkey_id, monkey.items)
            print()
        for monkey in monkey_list:
            monkey.inspect_and_throw_items(monkey_list, divider=1, reduce_number=prev_lcm)

    most_active_monkeys = [current_monkey.num_inspected_items for current_monkey in monkey_list]
    most_active_monkeys.sort()
    print(most_active_monkeys)
    print(most_active_monkeys[-1] * most_active_monkeys[-2])
