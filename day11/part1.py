import re


def find_numbers(string):
    return list(map(int, re.findall(pattern='\d+', string=string)))


class Monkey:
    def __init__(self):
        self.monkey_id = None
        self.items = []
        self.operation_type = None
        self.operation_number = None
        self.test_number = None
        self.next_monkey_id_true = None
        self.next_monkey_id_false = None
        self.num_inspected_items = 0

    @staticmethod
    def from_text(description):
        name, items, operation, test_number, next_monkey_true, next_monkey_false = description.splitlines()
        new_monkey = Monkey()
        new_monkey.monkey_id = find_numbers(name)[0]
        new_monkey.items = find_numbers(items)
        new_monkey.operation_type = re.findall(pattern='[\+\*]', string=operation)[0]
        new_monkey.operation_number = operation.split(' ')[-1]
        new_monkey.test_number = find_numbers(test_number)[0]
        new_monkey.next_monkey_id_true = find_numbers(next_monkey_true)[0]
        new_monkey.next_monkey_id_false = find_numbers(next_monkey_false)[0]
        return new_monkey

    def inspect_and_throw_items(self, other_monkeys, divider, reduce_number=None):
        for item in self.items:
            self.num_inspected_items += 1
            if reduce_number:
                item = item % reduce_number
            worry_level_result = self.calc_worry_level(item) // divider
            if worry_level_result % self.test_number == 0:
                self.throw(worry_level_result, other_monkeys, self.next_monkey_id_true)
            else:
                self.throw(worry_level_result, other_monkeys, self.next_monkey_id_false)
        self.items = []

    @staticmethod
    def throw(item, other_monkeys, monkey_id):
        for other_monkey in other_monkeys:
            if other_monkey.monkey_id == monkey_id:
                other_monkey.items.append(item)
                return
        raise ValueError(f'Monkey id {monkey_id} not found!')

    def calc_worry_level(self, item):
        if self.operation_number == 'old':
            number = item
        else:
            number = int(self.operation_number)
        if self.operation_type == '+':
            return item + number
        elif self.operation_type == '*':
            return item * number
        raise ValueError(f'Unknown operation type {self.operation_type}')


if __name__ == '__main__':
    monkey_list = []
    num_rounds = 20
    with open('monkeys.txt') as f:
        for monkey_text in f.read().split('\n\n'):
            monkey_list.append(Monkey.from_text(monkey_text))
    for i in range(num_rounds):
        print('Round', i)
        for monkey in monkey_list:
            print('Monkey', monkey.monkey_id, monkey.items)
        print()
        for monkey in monkey_list:
            monkey.inspect_and_throw_items(monkey_list, divider=3)

    most_active_monkeys = [current_monkey.num_inspected_items for current_monkey in monkey_list]
    most_active_monkeys.sort()
    print(most_active_monkeys)
    print(most_active_monkeys[-1] * most_active_monkeys[-2])
